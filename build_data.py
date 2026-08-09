#!/usr/bin/env python3
"""Generates data.json for the Kyndryl fit-map page.
The roles render as tabs on one page and share a single evidence pool.
Single source of truth: edit this, run `python3 build_data.py`, and data.json
is rewritten. (Or just edit data.json directly, this is a convenience.)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Evidence (title + text shown to the reader; shared across all tabs) ----
evidence = {
  "ev-service-design": {"title": "7+ Years of Service Design", "text": "7+ years as a practicing service designer with an advanced degree in the specialty, but 13+ years designing how people move through complex products, services, and operations — including service design, innovation, and design strategy roles across multiple startups and Fortune 500 corporations; Delta Air Lines and Bayer."},
  "ev-13yrs": {"title": "13 Years of Client-Facing Delivery", "text": "My career began with 6 years leading client work in film and TV + advertising and music videos. Since then, 7 years of client implementation, consulting, and stakeholder management across startups, nationwide franchises, Delta Air Lines, and Bayer."},
  "ev-ma": {"title": "Design-First Business Strategy M.A.", "text": "M.A. in Design-First Business Strategy from SCAD's De Sole School of Business Innovation — essentially an MBA crossbred with service design, built for intrapreneurship and using design thinking to influence decision making. My B.F.A. is from SCAD as well; business for film and television."},
  "ev-credentials": {"title": "Additional Credentials & Training", "text": "Beyond my Design-First Business Strategy M.A. and my B.F.A. in entertainment business from SCAD, I am a Gallup Certified Strengths Coach. Additionally, I have a certificate in Design for Urban Mobility from the University of Amsterdam, and have done multiple innovative business trainings in niche and offer design via Traffic & Funnels and offers, leads, and business models via Acquisition.com and their events."},
  "ev-wide-industry": {"title": "Wide Industry Experience", "years": "14+ years experience", "text": "Experience across 10+ industries and hundreds of niche personas across unrelated service verticals — film and TV, agriculture, counseling, fitness, hospitality, education, logistics, sports entertainment. I learn fast, dive deep, and have a proven ability to onboard quickly to and lead in any business domain."},
  "ev-travel-30": {"title": "Happy to Travel", "text": "Would love to. 30% on the road interests me."},
  "ev-travel-40": {"title": "Happy to Travel", "text": "Would love to. 40% on the road interests me."},

  "ev-blueprinting": {"title": "Service Blueprinting", "years": "7+ years experience", "text": "Built service blueprints at every scale from a 450-point blueprint for a startup's information architecture and executive decision making to a 20,000+ point global, enterprise level blueprint to identify service, product, technology, and operational gaps and opportunities at Bayer.", "link": "https://www.hance.work/Local-Enterprise-Level-Service-Blueprint-74f9ecfa9f4a4873be1b909a7f5e37d8?pvs=25"},
  "ev-present-future": {"title": "Present State vs Future State", "years": "10+ years experience", "text": "I map the present state of an organization, business unit, or stakeholder journey to design the future state. The global blueprinting effort at Bayer existed to identify the present state of our tech stack and operational interactions and then make recommendations for future state: we delivered a present state map and a future state map. I did the same at Dryland Revival, mapping our current processes and then identifying new product and service opportunities for our customers and better ways of working for our teams."},
  "ev-journey-mapping": {"title": "Journey Mapping", "years": "7+ years experience", "text": "I have mapped journeys across startups, national franchises, and the Fortune 500. At Bayer I facilitated a global journey mapping effort spanning North America, Europe, and Asia-Pacific, 2,250 journey points across 27 teams, that cut environmental toxin risk 70% and raised workplace safety 30% within two quarters. At Dryland, the customer and employee journeys inside our 450 point blueprint became the source for our playbooks, org design, and project management system. I led the migration of Bayer's global, enterprise level blueprint from Miro to TheyDo so the journeys could be managed more accurately and dynamically.", "link": "https://www.hance.work/Global-Journey-Mapping-Effort-228e643935ea43aab50ee95d8f56305f?pvs=25"},
  "ev-systems-mapping": {"title": "Systems Mapping", "years": "13+ years experience", "text": "I build maps that help teams see the bigger picture and communicate and make decisions more efficiently. At Dryland Revival, I built a map with 100+ interaction points across all five departments. I have built comparative org charts that let a nationwide franchise see its restructure clearly enough to reorganize without a single layoff, current and future state organizational maps for entire Fortune 500 divisions, and the visual maps of crew, cast, and equipment that ran thousands of production days across six years in the film industry."},
  "ev-ia": {"title": "Information Architecture", "years": "10+ years experience", "text": "I structure information so people, teams, and technology can equally increase efficiency with it. I have been designing the automations and information architecture of project management systems since working in the film industry, and recently developed enterprise-wide IA for PM systems at Dryland Revival. At Bayer, I designed the information architecture of the agentic persona service, and mapped the data source architecture of the global, enterprise level future state service blueprint and tech stack recommendations. Today I architect AI native, tool agnostic knowledge systems with project flow automations and documentation structures for both human and agent ease of retrieval."},
  "ev-systems-thinking": {"title": "Systems Thinking", "years": "13+ years experience", "text": "I live in a constant state of mapping systems in my head. It is what allowed me to excel at the rapid, leadership-level decision making of being an Assistant Director on set in the film industry and helps me see consequences of business decisions that most others don't. When I walk into a room, a team, or a company, I have the system mapped in my head immediately. The blueprints, frameworks, and playbooks I design are made to help others act with the level of empathy their stakeholders need."},
  "ev-root-cause": {"title": "Root Cause Solutioning", "years": "13+ years experience", "text": "I'll spend an entire day on a single problem, because I know that resolving the system instead of the symptom saves days, weeks, or months of work later. And not just for me, but for entire teams, divisions, or organizations as a whole."},
  "ev-prototyping": {"title": "Prototyping", "years": "13+ years experience", "text": "Build context appropriate prototypes, low to high fidelity, to make ideas testable and accessible to feedback and usability. Some examples: agentic user personas built and validated inside a Fortune 500 before commercial AI tools existed, sustainable business model prototypes for Delta, and the Fans First experiences the Savannah Bananas scaled to global fame. Not to mention the rapid prototyping of sites, tools, maps, and apps in the AI era."},
  "ev-experience-design": {"title": "Experience Design", "years": "13+ years experience", "text": "I have been designing experiences professionally for over a decade. At the end of six years in the entertainment industry, I helped develop and execute the prototype \"Fans First\" experience that became the standard the Savannah Bananas then scaled to global fame. Before that, I employed experience design principles to innovate on decades old traditions as Program Director of a 1,500 person summer camp, and taught those principles to the next generation of camp leaders. Since then, I designed multi-stakeholder experiences at Delta Air Lines and Campus Carriers, lead the end-to-end farmer experience at Bayer across marketing, product, and portal surfaces, and employee and customer experiences at Bayer, Dryland Revival, and the national franchises I work with at AGS."},
  "ev-product-leadership": {"title": "End-to-End Product Leadership", "years": "7+ years experience", "text": "UX Lead on Bayer's end-to-end customer site rebuild, acting as the design side Product Manager — from the public marketing pages through the post log in customer portal — driving a 35% increase in product and service opportunities and leading user acceptance testing across the North American user base."},
  "ev-tech-stack": {"title": "Tech Stack Blueprinting", "years": "7+ years experience", "text": "Bayer's global enterprise blueprinting effort was tech stack blueprinting at the largest possible scale: mapping the present state of every tech stack, persona, and operational interaction across multiple countries, then delivering future state recommendations that exposed redundant systems and unserved gaps. At Dryland, the 450 point blueprint drove the design and redesign of our entire tech stack, from the original ClickUp buildout to a Monday.com rebuild and the Zapier automations connecting it all. I still do this for clients today, including the end-to-end service blueprint and strategic recommendations that determined a hospitality franchise's tech stack roadmap for multi-location build outs."},
  "ev-design-standards": {"title": "Design Standards", "years": "4+ years experience", "text": "Authored Bayer's Universal Design Principles, adopted across every platform under the Head of Design for the $27B Crop Sciences division."},
  "ev-design-fluency": {"title": "Design Fluency", "years": "7+ years experience", "text": "I'm a trained service designer with a background in operations and leading teams. My fluency in design work allows me to ask the right questions and spot risk early, because I've built the blueprints, run the research, and facilitated the workshops myself."},

  "ev-research": {"title": "Research & Discovery", "years": "7+ years experience", "text": "Discovery is where I start every engagement and conversation. Masters level training + 7 years of real world experience in ethnographic field research, stakeholder interviews, contextual inquiry, and journey mapping to turn workforce challenges into actionable solutions."},
  "ev-insights": {"title": "Prioritization via Insights", "years": "13+ years experience", "text": "As a strategist, I prioritize actions and roadmaps via active analysis. This is a muscle that has been being trained since running film sets and having to make significant, long term decisions live in the moment. I was then given the tools and additional frameworks in grad school where my research and prioritization skillsets were trained intentionally. At Bayer, ethnographic user discovery overturned product decisions external consultancies had built from business stakeholder input alone. At Delta, passing our concepts through a business model canvas reset the entire direction of the engagement. At Dryland, interviews with team leads redirected employee retention efforts, and now I guide executive teams in efforts that affect their entire company."},
  "ev-research-tools": {"title": "Research & Analytics Tools", "years": "7+ years experience", "text": "Masters level training + 7 years of real world experience in research and analysis as well as their most premium tools: MAXQDA for qualitative coding, DisplayR and QuestionPro for survey and quantitative analysis, plus the discovery toolkit of interviews, contextual inquiry, and ethnographic field research behind them."},
  "ev-testing": {"title": "Testing & Validation", "years": "7+ years experience", "text": "Led User Acceptance Testing across a Fortune 500's North American user base, built agentic personas validated above 80% by 20+ year subject matter experts that cut UAT failures, and always run usability and prototype testing to pressure test ideas before they ship.", "link": "https://www.hance.work/User-Testing-Strategic-Recommendations-9f073d6ea0bb4bd1bef08d176895dd10?pvs=25"},
  "ev-vendor-selection": {"title": "Vendor Selection", "years": "13+ years experience", "text": "Drove the research and strategy that anchored Bayer's selection of its enterprise Customer Data Platform vendor, then structured the governance team that integrated it, translating between what the business needed, what the technology could do, and what the users would actually adopt. I have been selecting technologies and vendor partners since my film days, that could look like researching, building relationships with, and engaging 10+ external vendor partnerships on a single branded film. At Dryland, I selected our project management platform, built it end to end in ClickUp, then deliberately re-selected and rebuilt in Monday.com because the mobile experience served our field crews better. I regularly self train on unfamiliar enterprise software to the depth of evaluating vendor fit, and I evaluate against the workflows and journeys of all of the stakeholders, who will interact with the tool from different directions."},
  "ev-metrics": {"title": "Metrics Design", "years": "7+ years experience", "text": "Masters level training in metric determination: designing the right success metrics for the situation, then measuring against them. Fluent in OKRs, KPIs, NPS, adoption rate, time to launch, and satisfaction. Decision criteria that anchored client adoption logic in my work with Delta, the Franchise Criteria Canvas and priority matrices that gave a nationwide franchise an agreed standard for franchisee decisions, the SME validation threshold that gated Bayer's agentic personas before teams were allowed to rely on them, and the performance analytics, trackers, and dashboards Dryland ran on. Regularly measuring outcomes against the vision that was set: a 35% lift in product and service opportunities, a 30% rise in workplace safety, and 2% to 26% platform adoption in two months."},

  "ev-gtm": {"title": "Go-to-Market & Offer Design", "years": "7+ years experience", "text": "Structured the offer and go-to-market strategy for seven intrapreneurial and entrepreneurial ventures: an internal agentic tool at Bayer, sustainable products at Delta Air Lines, an education as a service line with Campus Carriers, the business model for Dryland Revival, multiple successful leadership practices, my franchise consulting business. Formal training in business modeling and GTM strategy (M.A. program at SCAD), niche and offer design (Traffic & Funnels) and offers, leads, and business models (Acquisition.com). I take an opportunity from value proposition to packaging, and into a working product or service."},
  "ev-biz-model": {"title": "Business Model Design", "years": "7+ years experience", "text": "Designed business models, tech stacks, and service models across many engagements: agentic tools within Bayer, sustainable business models for Delta's obsolete beverage carts, a construction-science startup's operating model, a B2B2C education as a service for Campus Carriers, a hospitality franchise's multi-location tech roadmap, and five personal ventures grown to profitability."},
  "ev-decision-frameworks": {"title": "Decision Frameworks", "years": "13+ years experience", "text": "I am a strategic framework and decision model library, and I use these tools to help teams uncover information, connect dots, and communicate clearly. If I don't have a tool perfect for helping a team make a decision, I design one in the moment. I've been building these tools myself and using them with teams professionally since working in the film industry, so I have a backlog of hundreds of models and frameworks going back 10+ years, not to mention the hundreds that I have collected from other great thought leaders."},
  "ev-strategic-advising": {"title": "Strategic Advising", "years": "13+ years experience", "text": "My strategic advising goes back to film and TV, where the producer's first job is advising the client on their own vision: what is actually possible within the timeline and budget, and what it will take to get there. Since then: primary client contact for Delta Air Lines leading a sustainability marketing effort, almost eight years of coaching leaders through my own practices, and advising for franchisees and franchisors today."},
  "ev-process-optimization": {"title": "Process Optimization", "years": "13+ years experience", "text": "My background in film means that the first half of my career required doing literally unbelievable things with scarce resources. Now, I reengineer systems to allow for the streamlining of resources that will exercise the greatest efficiency. I helped a university logistics operation restructure for a 60% resource reduction, built a startup playbook library that lifted efficiency 80% and removed the CEO from lower-level decisions, and developed operating cadences and management systems that kept teams aligned through rapid growth in both my entertainment industry days and my startup experiences."},

  "ev-change": {"title": "Change Management", "years": "12+ years experience", "text": "Drove change and adoption in resistant systems my entire career: from navigating day-to-day and hour-by-hour changes on film sets to innovating decades old traditions while keeping the soul of the experience at a 1,500 person summer camp, including a decade old training program replaced with modern methods, creating a 67% year over year retention lift; a nationwide counseling franchise led through restructuring across states without a single layoff; a startup org redesign that doubled revenue and quadrupled headcount; moving a construction field crew into modern technology in the context of a phone based project management system; and leading a Fortune 500 AI platform from 2% to 26% adoption in two months."},
  "ev-new-revenue": {"title": "New Revenue Lines", "years": "13+ years experience", "text": "I have pioneered new revenue lines across startups, franchises, and the Fortune 500. Developed a B2B2C education as a service line at Campus Carriers, owned end to end from primary market research through curriculum design, offer design, and pre-launch partnerships across seven partner universities. New service offerings designed and launched at Dryland Revival through a growth run that doubled revenue year over year for three years. Sustainable business models for thousands of Delta's obsolete beverage carts. An operations and marketing transformation at a physical health franchisee that opened the path to a second location. And my own ventures: a bicycle rental marketplace for a university, a community based product business grown to profitability, a vending machine business grown to profitability and exited, and multiple coaching and consulting practices grown to recurring five figure months."},
  "ev-biz-dev": {"title": "Business Development", "years": "10+ years experience", "text": "Built three consulting and coaching practices from scratch — structuring the offer, pricing, and go-to-market to land clients from day one, and led the business development that kept each running for 3+ years with consistent five-figure engagements. Led project development in the film industry before that, and led an effort selling an agentic persona service intrapreneurally at Bayer."},

  "ev-concurrent-pm": {"title": "Concurrent Project Management", "years": "10+ years experience", "text": "Owned film and TV productions end to end as the client's point of contact, delivering on time and on budget while running an average of six concurrent productions, peaking at ten to twelve multiple times. Currently managing multiple engagements with AGS."},
  "ev-client-delivery": {"title": "End-to-End Client Delivery", "years": "13+ years experience", "text": "Six years in film and TV owning productions end to end as the client's point of contact, on time and on budget across roughly 50 productions, including a branded film for Hamilton Watches spanning 30+ crew, 20+ talent, eight locations, and ten-plus vendor partners. Then Delta, where I was the primary contact between client and team, presenting at corporate while translating business needs to the creative team in the studio. Today I own consulting engagements end to end for franchisors, franchisees, and service businesses, from scoping and discovery through implementation and adoption."},
  "ev-engagement-ownership": {"title": "Engagement Ownership", "years": "13+ years experience", "text": "I lead multiple concurrent client engagements end to end, owning scoping, timeline, and delivery from discovery through handoff. This skillset developed in film and TV first, where our crew averaged six productions at a time and peaked between ten and twelve. I also owned multiple engagements with business stakeholders as a design leader at Bayer and Delta Airlines."},
  "ev-inherited": {"title": "Evaluating Inherited Work", "years": "10+ years experience", "text": "I am regularly handed someone else's work and asked to move forward from where they left off. This was common in the film industry and most of my efforts in other operational capacities like at Campus Carriers and Greene Family Camp. At Bayer, my first assignment on the operations platform was user acceptance testing with zero context on products built before we arrived. Additionally, my first assignment with the customer platform was to take over ownership of the primary user experience for the end-to-end farmer site rebuild, where I immediately discovered a gap in designing for user trust by the external consultancies. Entering a project without the builders' context is an advantage, because most users of a product, service, or system do not have that context either."},
  "ev-early-risk": {"title": "Early Risk Flagging", "years": "13+ years experience", "text": "Skilled at identifying delivery risk early in unfamiliar domains — a habit built through six years of film sets where the surprises required quick production-wide changes, seven years in summer camping where one lightning strike could change the plans for 500 kids for a whole day, and running operations across multiple startups."},
  "ev-rapid-domain": {"title": "Rapid Domain Learning", "years": "13+ years experience", "text": "Joined into a Fortune 500 knowing nothing about agriculture and was shipping across four platforms within a year. Joined Dryland knowing nothing about construction sciences and grew the business to profitability within two years. Have done relevant and successful consulting work in 10+ unfamiliar domains."},
  "ev-workstreams": {"title": "Multiple Workstreams", "years": "13+ years experience", "text": "Like my time in the entertainment industry, summer camping, and consulting, my role at Bayer was constantly in flux. I started as the UX lead for the farmer experience, became a design strategist for the operations platforms, then lead strategist for the generative AI effort, turning a six month contract into 18 months by continuing to be useful. I ramp quickly on new problems."},
  "ev-agile": {"title": "Agile Experience", "years": "4+ years experience", "text": "Worked inside agile product teams across four Bayer platforms: refined backlogs, aligned hundreds of technical stories to user needs, led user acceptance testing across the North American user base, then built out the scrum board — writing all the stories and leading scrum — for a legacy platform team."},

  "ev-mentorship": {"title": "Mentorship Experience", "years": "12+ years experience", "text": "Ran training and development for a 250 person camp staff, redesigning a program that lifted retention 67% year over year, am Gallup certified, trained leadership coach with almost eight years running my own coaching practice, and spent six years in film identifying underutilized talent, developing them through on set mentor matching, and enabling them to lead their own crews."},
  "ev-coaching": {"title": "Coaching", "years": "7+ years experience", "text": "Gallup Certified Strengths Coach trained in behavior and relationship psychology; almost eight years of facilitating leadership development in the context of empathy strategies and emotional intelligence professionally. Built a leadership development practice from scratch to five figure revenue months within six months, running and iterating workshops and facilitation opportunities since. I've coached hundreds of high school and college students through multi-month social-emotional learning and leadership programs, and hundreds of others through weekend retreats, cohorts, and high ticket 1:1 men's work, with custom tools for mental and emotional processing developed in line with my systems and design thinking background."},
  "ev-psych": {"title": "Human Behavior & Psychology", "years": "12+ years experience", "text": "Gallup Certified Strengths Coach trained in behavior and relationship psychology. This guides my deep empathy for user behavior, and my ability to influence change without authority. Eight years of teaching emotional intelligence and social emotional learning professionally means I can read motivations, needs and expectations, and emotions as a professional expertise, not a personality trait. I use that background to shape desirability and adoption."},

  "ev-xfn": {"title": "Cross-Functional Leadership", "years": "13+ years experience", "text": "I have led across functions and disciplines my entire career. On film sets, every department head came to me as the hub for information, prioritization, and decision making across thousands of crew, cast, and vendors. At Delta, I led a cross-cultural team spanning eight countries and nine disciplines while owning budget, timelines, and the client relationship, presenting at corporate and translating business needs to the creative team in the studio. At Bayer, I aligned 27 teams that did not report to me across North America, Europe, and Asia-Pacific. At Dryland, all six teams ran on the operating systems I developed."},
  "ev-translator": {"title": "Cross Discipline Fluency", "years": "13+ years experience", "text": "Fluent in business, design, and engineering languages. I love translating business jargon to design requirements, engineering capabilities to business possibilities, and design visions to engineering roadmaps. This is the product and service version of what I did as a producer and assistant director in the entertainment industry in the first half of my career."},
  "ev-facilitation": {"title": "Workshop Facilitation", "years": "12+ years experience", "text": "I have practiced facilitation professionally for over a decade. Hundreds of design thinking workshops from 5 to 150 people at Bayer, where Miro selected me as the sole Enterprise Advocate for a company of ~100,000 people. Staff trainings, development programming, and multi-day events for a 250 person staff at one of the country's largest summer camps. Eight years of leadership retreats, cohorts, and group trainings through my own practices, from high school and college students to the men's work I facilitate today. And the working sessions I currently run with franchise corporate teams and franchisees."},
  "ev-speaking": {"title": "Public Speaking & Presentations", "years": "10+ years experience", "text": "Over a decade of live presentations, from pitch decks in Fortune 500 corporate rooms to multi-day retreats, scaled coaching programs, and live events for a 1,500-person camp. Comfortable commanding a room of five people to five thousand."},
  "ev-exec-alignment": {"title": "Executive Alignment", "years": "10+ years experience", "text": "At Bayer, I developed an agentic AI experience and sold it internally through months of workshops, demos, and one on one influencing before getting the greenlight to build. At Delta, I was the primary client contact, presenting status updates and pitch decks regularly to corporate. As a franchise consultant, I work directly with CEOs, executive teams, and franchisors. At Dryland, I was the CEO's first conversation and advisor on every major decision. The first half of my career in film was aligning clients and directors on what was actually possible within the timeline and budget."},
  "ev-storytelling": {"title": "Storytelling & Executive Narrative", "years": "10+ years experience", "text": "Ten years writing 20 to 50 pages a week of creative and business content, from user stories to executive strategy. As Delta's primary client contact I presented status updates and pitch decks in corporate rooms while translating business needs to the creative team, and I sold an agentic AI build to Bayer executives through months of workshops, demos, and one-on-one narrative."},
  "ev-strategic-writing": {"title": "Strategic Writing & Documentation", "years": "10+ years experience", "text": "Built upon a practice of writing 20 to 50 pages a week, I have delivered hundreds of scripts and character driven narratives, as well as hundreds of pages of strategic documentation, philosophical essays, user stories, and executive strategy. I authored Bayer's Universal Design Principles, adopted across every platform in the division, the Customer Data Platform strategy documentation that anchored vendor selection at the enterprise level, and the AI Strategy Playbook shipped in 20+ languages. Today I write the documentation depth that powers tool agnostic AI knowledge management."},
  "ev-curriculum": {"title": "Curriculum & Learning Design", "years": "7+ years experience", "text": "Designed learning programs and curricula end to end: a leadership curriculum across seven partner universities, multi-month social emotional learning and leadership programs and retreat curricula for high school and college students, high ticket 1:1 men's work including course material, custom processing tools, and interaction cadences, the cohort and retreat programming I still run for men in their 20s, 30s, and 40s, a redesigned staff training program at a 1,500 person camp that lifted retention 67% year over year, and AI enablement content, guides, and quick reference materials for thousands of Fortune 500 users."},

  "ev-adoption": {"title": "Tool and AI Adoption", "years": "10+ years experience", "text": "Adoption is a design problem. At Bayer, I took a Fortune 500's internal AI platform from 2% to 26% adoption in two months, by treating it as a competence problem rather than a trust problem. Beyond that, I developed an agentic persona service that multiple anti-AI teams started using daily, a project management system that construction field crews actually used on their phones, the migration of Bayer's global blueprint from Miro to TheyDo that matured design thinking across the enterprise through ease of discovery for customer journey maps, and currently lead teams from Notion, Dropbox, and Google Drive into tool agnostic markdown systems that increases their AI usage. This passion started in the film industry where I led the adoption of on-set and pre-production technologies across teams and departments."},
  "ev-ai-training": {"title": "Global AI Training", "years": "3+ years experience", "text": "Authored Bayer's AI Strategy Playbook and led its global dissemination in 20+ languages to thousands of internal users across business, engineering, design, and HR — training entire departments of the business from Indonesia to Brazil in a single quarter.", "link": "https://www.hance.work/Generative-A-I-Playbook-bb68ca8c80d840e5be083136a0b88f92?pvs=25"},
  "ev-ai-agents": {"title": "Building AI Agents", "years": "3+ years experience", "text": "Pioneered an agentic persona service at Bayer in 2023, before commercial agents were available. I built AI models of users our design team couldn't otherwise reach, wired into Microsoft Teams before commercial AI integrations existed for the company's stack. The workflow produced high fidelity user representations rapidly, validated by SMEs above 80% accuracy, and significantly reduced UAT failures across the teams that used them. That was over 3 years ago. Imagine what I can do with your data and Claude's newest features.", "link": "https://www.hance.work/A-I-Persona-Prototypes-43575337f52c4cecaf4fdd871e5aa41e?pvs=25"},
  "ev-agentic-ops": {"title": "Agentic Operations Design", "years": "3+ years experience", "text": "Currently transforming business operations through agentic experience design alongside human and AI skill development, increasing the efficiency and accuracy of leaders, teams, and individual contributors. I own transformation engagements from scoping and discovery through implementation and adoption, and build AI-native, tool-agnostic knowledge management systems for creative and operational teams, architected for both human and agent ease of retrieval."},
  "ev-responsible-ai": {"title": "Responsible AI", "years": "3+ years experience", "text": "I've been integrating AI into human systems since before commercial integrations existed — agentic personas validated by 20+ year subject-matter experts above 80% accuracy before teams were allowed to rely on them. I've also led stakeholder AI education from Indonesia to Brazil, and designed governance gates for agents to reduce failures and overstepping."},
  "ev-ai-tool-eval": {"title": "AI Tool Evaluation", "years": "4+ years experience", "text": "Regularly self train on unfamiliar enterprise software to the depth of evaluating vendor fit, proven at the Fortune 500 level and across startups. Drove a Fortune 500's Customer Data Platform vendor selection and gave strategic input on its internal LLM platform build. My goal is to identify the right tool for the right job and the right persona."},
  "ev-ai-product": {"title": "AI Product Strategy", "years": "3+ years experience", "text": "Led product strategy on the build out and adoption of Bayer's internal LLM platform pre-AI-boom, impacting design and product decisions and leading user testing. That work continues today as the core of my consulting practice. I build agentic, tool agnostic knowledge systems for creative and operational teams, design the prompt, workflow, and rule configurations they run on, and treat retrieval quality and human authored context as the leverage priority.", "link": "https://www.hance.work/A-I-Product-Roadmap-d042f4d986e5441bbb80b5e5ea4bd018?pvs=25"},
  "ev-ai-reliability": {"title": "AI Reliability & Quality", "years": "3+ years experience", "text": "Build AI systems that perform reliably in production by treating the knowledge layer as the priority. SME written or validated content over endless prompt tuning, corpus audits for the percentage actually authored by humans, retrieval and validation management and measurement, and active guarding against the context dilution that comes from LLMs overwriting good context over time. Proven at the Fortune 500 level at Bayer, where agentic personas grounded on internal research and customer data were validated above 80% accuracy by subject matter experts with 20+ years in the field."},
  "ev-rd-lab": {"title": "Personal R&D Lab", "years": "16+ years experience", "text": "My personal life is a constantly running R&D lab — I've been ramping on a new technology at least once a quarter since high school, and my current operating system pairs agentic AI workflows with a digital brain to extend what I can do. I love unfamiliar domains and emerging tech."},

  "ev-playbooks": {"title": "Playbook Writing", "years": "10+ years experience", "text": "Built an operations playbook at Campus Carriers that cut resource needs 60%, an entire startup playbook library that lifted efficiency 80% and removed the CEO from lower-level decisions at Dryland Revival, and a Fortune 500 AI strategy playbook shipped in 20+ languages at Bayer. This was all built on the foundation of playbook building for my teams in the film industry."},
  "ev-pm-system": {"title": "PM System Design", "years": "10+ years experience", "text": "I have designed and facilitated project management systems my whole career. In film, I designed the project management system that managed hundreds of productions and kept projects on time and on budget while our crew averaged six productions at a time, peaking between ten and twelve. At Dryland, I designed the automations and information architecture end to end: built in ClickUp, rebuilt in Monday.com and run on Zapier automations. Prioritizing one click steps for every stakeholder in each process. At Bayer, I built out the scrum board and wrote all the stories for a legacy platform team that had no user stories or change tracking. Today I build project management systems in Notion and Claude for clients and my own operation."},
  "ev-enterprise-migration": {"title": "Enterprise Tool Migration", "years": "4+ years experience", "text": "Led the migration of Bayer's global, enterprise level service blueprint from Miro to TheyDo — customer journey enablement at the enterprise level. I have also led multiple teams in migrating from Notion, Dropbox, Google Drive, and other knowledge sources to Obsidian via markdown strategy to become tool agnostic super users of their own information."},

  "ev-live-events": {"title": "Live Event Operations", "years": "14+ years experience", "text": "A decade producing live audience experiences — a full season of 100% sold out Savannah Bananas games, six years of music festival operations, and years of weekly events for a 1,500 person summer camp. Currently producing community gatherings."},

  "pf-full": {"title": "Full Portfolio", "text": "Twelve public case studies across service blueprints, journey maps, systems maps, AI strategy, and UX — each one walks through the process, the deliverables, and the impact.", "link": "https://www.hance.work/"},
  "pf-global-blueprint": {"title": "Global Enterprise Service Blueprint", "text": "Bayer's 20,000+ point global service blueprint mapping tech, personas, and interactions across countries to surface redundancies and gaps.", "link": "https://www.hance.work/Global-Enterprise-Level-Service-Blueprint-cd937db4cb344b318bae4c6d1e7ca9fa?pvs=25"},
  "pf-local-blueprint": {"title": "Local Enterprise Service Blueprint", "text": "A focused enterprise service blueprint mapping a business's systems and interaction points end to end.", "link": "https://www.hance.work/Local-Enterprise-Level-Service-Blueprint-74f9ecfa9f4a4873be1b909a7f5e37d8?pvs=25"},
  "pf-journey": {"title": "Global Journey Mapping Effort", "text": "A 27-team global journey map producing 2,250 journey points and new processes on a confidential European compliance project.", "link": "https://www.hance.work/Global-Journey-Mapping-Effort-228e643935ea43aab50ee95d8f56305f?pvs=25"},
  "pf-eraf": {"title": "Systems Flow (ERAF) Map", "text": "A systems-flow map of 100+ interaction points that helped siloed teams see their role in the larger business — and kept employees who were ready to quit over 'bad communication.'", "link": "https://www.hance.work/Systems-Flow-ERAF-Map-74cfa7e910564777a9883a55f066d4f9?pvs=25"},
  "pf-cdp": {"title": "Customer Data Platform Roadmap", "text": "The use cases and roadmap, built from the customer-experience perspective, that anchored a Fortune 500's Customer Data Platform vendor selection.", "link": "https://www.hance.work/Customer-Data-Platform-Roadmap-0d65a3c99943497e9c969160e33742a2?pvs=25"},
  "pf-ai-roadmap": {"title": "A.I. Product Roadmap", "text": "Product roadmap for a Fortune 500's internal AI platform, defining the use cases and the path to adoption.", "link": "https://www.hance.work/A-I-Product-Roadmap-d042f4d986e5441bbb80b5e5ea4bd018?pvs=25"},
  "pf-genai-playbook": {"title": "Generative A.I. Playbook", "text": "The AI strategy playbook that drove adoption from 2% to 26%, shipped in 20+ languages to thousands of users.", "link": "https://www.hance.work/Generative-A-I-Playbook-bb68ca8c80d840e5be083136a0b88f92?pvs=25"},
  "pf-legacy-ux": {"title": "Legacy Software UX Strategy", "text": "Restructured forms, progress indicators, and language to make a legacy platform more efficient and usable.", "link": "https://www.hance.work/Legacy-Software-UX-Strategy-e189dab0fccc4d088f0f8e2a22b009a9?pvs=25"},
  "pf-prompt": {"title": "Prompt Engineering Strategic Design", "text": "A prompt engineering approach and template that let non-technical stakeholders across the company use generative AI effectively for the first time.", "link": "https://www.hance.work/Prompt-Engineering-Strategic-Design-40891c882c00477e936743a5d0657ddc?pvs=25"},
}

def ph(pid, text, ev):
    return {"id": pid, "text": text, "evidence": ev}


# ---- Tab 1: Senior Experience Strategist (primary, default on load) ----
def strategist_prose():
    return [
      {"type": "h2", "text": "The Role"},
      {"type": "p", "segments": [
        "As a Senior Experience Strategist in Kyndryl Vital, you will ",
        ph("es-gtm", "shape the go‑to‑market strategy",
           ["ev-gtm", "ev-biz-model"]),
        " and ",
        ph("es-presales", "create high‑impact pre‑sales content",
           ["ev-biz-dev", "ev-storytelling"]),
        " that fuels Customer Experience (CX) pipeline growth. You will translate market needs and human‑centered approaches into ",
        ph("es-offerings", "compelling offerings, narratives, and solution frameworks",
           ["ev-gtm", "ev-decision-frameworks", "ev-strategic-writing"]),
        " that empower sellers, differentiate Kyndryl in the market, and ",
        ph("es-win-deals", "win deals",
           ["ev-biz-dev"]),
        ". This role blends ",
        ph("es-blend", "strategic thinking, customer empathy, and storytelling excellence",
           ["ev-systems-thinking", "ev-psych", "ev-storytelling"]),
        " to ",
        ph("es-buying", "influence buying decisions",
           ["ev-exec-alignment", "ev-decision-frameworks"]),
        " and ",
        ph("es-revenue", "accelerate revenue",
           ["ev-new-revenue"]),
        "."
      ]},

      {"type": "h2", "text": "Who You Are"},
      {"type": "p", "segments": [
        "You bring ",
        ph("es-growth-mindset", "a growth mindset",
           ["ev-rd-lab", "ev-rapid-domain"]),
        ", ",
        ph("es-cx-passion", "a passion for solving customer experience problems",
           ["ev-experience-design", "ev-service-design"]),
        ", ",
        ph("es-unique-lens", "a knack for looking at familiar challenges through a unique lens",
           ["ev-root-cause", "ev-inherited"]),
        ", and ",
        ph("es-simplify", "the ability to simplify complexity into compelling narratives",
           ["ev-systems-mapping", "ev-storytelling"]),
        ". You ",
        ph("es-collaborative", "thrive in collaborative, cross-functional environments",
           ["ev-xfn"]),
        " and are energized by helping teams win in the CX market. You ",
        ph("es-experimentation", "embrace experimentation, human-centered thinking, and continuous learning",
           ["ev-prototyping", "ev-research", "ev-rd-lab"]),
        "."
      ]},

      {"type": "h2", "text": "Required Skills and Experience"},

      {"type": "li", "segments": [
        {"b": "Create Compelling Pre Sales Content"},
        ": ",
        ph("es-reusable-assets", "Develop resuable assets",
           ["ev-playbooks", "ev-decision-frameworks"]),
        ", ",
        ph("es-pitch-materials", "pitch materials, value propositions",
           ["ev-gtm", "ev-speaking"]),
        ", compelling POVs, ",
        ph("es-narratives", "storytelling frameworks, and executive-ready narratives",
           ["ev-storytelling", "ev-strategic-writing"]),
        " that clearly articulate ",
        ph("es-outcomes-impact", "customer outcomes and business impact",
           ["ev-metrics", "ev-translator"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Business + Tech + Experience"},
        ": You can ",
        ph("es-integrated-strategies", "create integrated experience strategies that blend business, technology, and user needs",
           ["ev-translator", "ev-tech-stack", "ev-experience-design"]),
        ", ",
        ph("es-customer-first", "advocating for a customer-first approach to ensure all experiences are intuitive and meet user needs",
           ["ev-insights", "ev-product-leadership"]),
        ", including ",
        ph("es-ai-capabilities", "applying AI-driven capabilities such as personalization or automation within defined solutions",
           ["ev-ai-product", "ev-ai-agents", "pf-cdp"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Business Acumen"},
        ": You ",
        ph("es-business-strategy", "understand business strategy and can connect it to experience",
           ["ev-ma", "ev-design-fluency", "ev-biz-model"]),
        " and ",
        ph("es-experience-led", "help others understand the value of experience-led outcomes",
           ["ev-exec-alignment", "ev-facilitation", "ev-design-standards"])
      ]},
      {"type": "li", "segments": [
        {"b": "Experience Optimization"},
        ": You can ",
        ph("es-optimize", "evaluate and recommend ways to optimize customer and employee experiences",
           ["ev-present-future", "ev-journey-mapping", "ev-process-optimization"]),
        ", including ",
        ph("es-moments", "moments that could be improved with self-serve, AI, automation, and empowerment across the end-to-end journey",
           ["ev-agentic-ops", "ev-pm-system", "ev-blueprinting"]),
        ", including leveraging AI, automation, and self-service capabilities to improve usability and efficiency."
      ]},
      {"type": "li", "segments": [
        {"b": "AI Use Case Contribution"},
        ": You contribute to ",
        ph("es-ai-use-cases", "identifying and shaping AI-enabled experience opportunities within projects",
           ["ev-ai-product", "ev-ai-agents", "pf-ai-roadmap"]),
        ", supporting senior team members in ",
        ph("es-feasibility", "evaluating feasibility and value",
           ["ev-ai-tool-eval", "ev-metrics"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Design and deliver solutions"},
        ": Create strategic deliverables such as ",
        ph("es-experience-maps", "experience maps",
           ["ev-systems-mapping", "pf-eraf"]),
        ", ",
        ph("es-user-journeys", "user journeys",
           ["ev-journey-mapping", "pf-journey"]),
        ", and ",
        ph("es-blueprints", "service blueprints",
           ["ev-blueprinting", "pf-global-blueprint", "pf-local-blueprint"]),
        " to ",
        ph("es-articulate-insights", "articulate insights and guide solution development",
           ["ev-insights", "ev-present-future"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Co-Creation"},
        ": You excel at ",
        ph("es-align-workshops", "aligning stakeholders through workshops and collaborative sessions",
           ["ev-facilitation", "ev-xfn"]),
        ". You’ve ",
        ph("es-future-state-sessions", "facilitated brainstorming / future-state innovation sessions and use case development",
           ["ev-present-future", "ev-decision-frameworks"]),
        " that ",
        ph("es-pocs", "foster experimentation and POCs/prototypes",
           ["ev-prototyping", "ev-ai-agents"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Storytelling"},
        ": You can ",
        ph("es-narrative", "build a compelling narrative and communicate clearly",
           ["ev-storytelling", "ev-speaking"]),
        " – rooted in a desire to ",
        ph("es-change-behaviors", "change mind, hearts and behaviors",
           ["ev-psych", "ev-change"])
      ]},
      {"type": "li", "segments": [
        {"b": "Conduct Research and Analysis"},
        ": You can ",
        ph("es-qual-quant", "design and conduct qualitative and quantitative research",
           ["ev-research", "ev-research-tools"]),
        ", ",
        ph("es-concept-eval", "concept evaluations",
           ["ev-testing"]),
        ", and competitive analyses – ",
        ph("es-trends", "identifying trends, opportunities, and potential threats",
           ["ev-insights", "ev-early-risk"]),
        " to ",
        ph("es-future-cx-vision", "inform the future state CX vision",
           ["ev-present-future"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Psychology"},
        ": You have a ",
        ph("es-human-behavior", "deep understanding of human needs and behavior",
           ["ev-psych", "ev-coaching"]),
        " (e.g. thoughts, expectations, motivations, perceptions, beliefs, emotions, etc.) to ",
        ph("es-desirability", "influence desirability, adoption, and culture",
           ["ev-adoption", "ev-change"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "AI and Data Ethics"},
        ": You ",
        ph("es-ai-ethics", "leverage AI tools while maintaining quality and ethical standards",
           ["ev-responsible-ai", "ev-ai-reliability"]),
        ", understanding key considerations such as bias, transparency, and ",
        ph("es-user-trust", "user trust in AI-enabled experiences",
           ["ev-inherited", "ev-adoption"]),
        "."
      ]},

      {"type": "h2", "text": "What you’ll need"},
      {"type": "li", "segments": [
        ph("es-seven-years", "7+ years in progressive, CX strategy focused consulting role",
           ["ev-service-design", "ev-13yrs"]),
        "; with ",
        ph("es-sales-delivery", "a blend of sales and delivery experience",
           ["ev-biz-dev", "ev-client-delivery"]),
        " preferred, bringing ",
        ph("es-cross-industry", "cross-industry perspectives and outside-in thinking/best practices",
           ["ev-wide-industry", "ev-rapid-domain"]),
        "."
      ]},
      {"type": "li", "segments": [
        ph("es-degree", "Undergraduate or graduate degree in service design, strategic design, innovation strategy,business administration, or a related field",
           ["ev-ma", "ev-credentials"]),
        "."
      ]},
      {"type": "li", "segments": [
        ph("es-ai-exposure", "Exposure to AI-enabled tools or solutions (e.g., generative AI tools, analytics platforms, or automation technologies) and their application in experience design",
           ["ev-ai-tool-eval", "ev-ai-agents", "ev-ai-training", "pf-prompt"]),
        " is a plus"
      ]},
      {"type": "li", "segments": [
        ph("es-travel", "Ability to travel up to 30% as business requires",
           ["ev-travel-30"])
      ]},
    ]


# ---- Tab 2: Senior Experience Designer ----
def designer_prose():
    return [
      {"type": "h2", "text": "The Role"},
      {"type": "p", "segments": [
        "An Experience Designer ",
        ph("ed-crafts", "crafts immersive and engaging experiences that connect people with environments, events, and interactions",
           ["ev-experience-design", "ev-live-events"]),
        ", focusing on how these experiences feel and unfold over time. This role involves ",
        ph("ed-needs-emotions", "understanding the needs and emotions of participants through research and testing",
           ["ev-research", "ev-testing", "ev-psych"]),
        " and ",
        ph("ed-collab-stakeholders", "collaborating with various stakeholders to bring these experiences to life",
           ["ev-xfn", "ev-facilitation"]),
        ". By ",
        ph("ed-sensory", "considering the emotional, social, and sensory aspects of an experience",
           ["ev-psych", "ev-live-events"]),
        ", Experience Designers aim to create memorable and impactful moments that leave lasting impressions."
      ]},
      {"type": "p", "segments": [
        "As an Experience Designer at Kyndryl Vital you will ",
        ph("ed-lead-initiatives", "lead design initiatives across a variety of projects",
           ["ev-concurrent-pm", "ev-workstreams"]),
        ", ensuring that solutions are innovative, user-friendly, and aligned with client objectives. You will ",
        ph("ed-client-relationships", "develop and maintain strong relationships with clients, acting as a trusted design advisor throughout the project lifecycle",
           ["ev-client-delivery", "ev-strategic-advising", "ev-engagement-ownership"]),
        ". You will ",
        ph("ed-guide-teams", "guide design teams",
           ["ev-design-standards", "ev-design-fluency", "ev-mentorship"]),
        " in the creation of high-quality visual and interactive designs, ",
        ph("ed-business-user-needs", "ensuring the final product meets business and user needs",
           ["ev-product-leadership", "ev-translator"]),
        "."
      ]},
      {"type": "p", "segments": [
        ph("ed-technical-feasibility", "Partnering with technical teams, you will balance creative ideas with technical feasibility",
           ["ev-translator", "ev-agile"]),
        ", ensuring designs are practical and scalable. You will ",
        ph("ed-own-process", "take ownership of the design process, from discovery and ideation to prototyping and user testing",
           ["ev-research", "ev-prototyping", "ev-testing"]),
        ", ensuring ",
        ph("ed-consistent-delivery", "consistent delivery of impactful designs",
           ["ev-engagement-ownership", "ev-concurrent-pm"]),
        "."
      ]},
      {"type": "p", "segments": [
        "You will ",
        ph("ed-ai-projects", "support complex projects that leverage AI to create innovative, user-centered experiences",
           ["ev-ai-agents", "ev-ai-product"]),
        ", ",
        ph("ed-ai-standards", "setting standards for human/AI interaction design and process adoption across teams",
           ["ev-design-standards", "ev-adoption", "ev-responsible-ai"]),
        "."
      ]},
      {"type": "p", "segments": [
        "You’ll ",
        ph("ed-advise-ai", "advise clients and teams on the strategic use of AI in design",
           ["ev-agentic-ops", "ev-ai-product"]),
        ", ",
        ph("ed-balance-ethics", "balancing innovation with usability and ethics",
           ["ev-responsible-ai", "ev-ai-reliability"]),
        ", and ",
        ph("ed-experimentation-culture", "foster a culture of experimentation with AI while ensuring human agency remains central",
           ["ev-adoption", "ev-prototyping"]),
        ". You will ",
        ph("ed-share-knowledge", "actively share your knowledge of AI in design with others as part of your leadership, empowering your team to grow their proficiency",
           ["ev-ai-training", "ev-mentorship", "ev-curriculum", "pf-genai-playbook"]),
        ", while ",
        ph("ed-own-expertise", "continuing to develop your own expertise",
           ["ev-rd-lab"]),
        "."
      ]},

      {"type": "h2", "text": "Required Technical and Professional Expertise"},
      {"type": "li", "segments": [
        {"b": "Human-Centered Design"},
        ": You have a ",
        ph("ed-hcd", "deep understanding of human-centered design methods and mindset",
           ["ev-service-design", "ev-ma", "ev-design-fluency"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Co-Creation"},
        ": You excel at ",
        ph("ed-cocreation", "aligning stakeholders through workshops and collaborative sessions",
           ["ev-facilitation", "ev-xfn"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Storytelling"},
        ": You can ",
        ph("ed-storytelling", "communicate clearly and compellingly",
           ["ev-storytelling", "ev-speaking"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "User Research"},
        ": You can ",
        ph("ed-user-research", "design and conduct generative and evaluative user research",
           ["ev-research", "ev-research-tools", "ev-testing"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Prototyping"},
        ": You can ",
        ph("ed-prototyping", "create context-appropriate, low-to-high fidelity prototypes",
           ["ev-prototyping"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Visual Communication"},
        ": You have ",
        ph("ed-info-design", "expertise in information design",
           ["ev-ia", "ev-systems-mapping", "pf-eraf"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "AI and Data Ethics"},
        ": You ",
        ph("ed-ai-ethics", "leverage AI tools while maintaining quality and ethical standards",
           ["ev-responsible-ai", "ev-ai-reliability"]),
        "."
      ]},
      {"type": "li", "segments": [
        {"b": "Importance Travel is Required"},
        " ",
        ph("ed-travel", "Up to 40% or two days a week",
           ["ev-travel-40"])
      ]},

      {"type": "h2", "text": "Preferred Professional and Technical Expertise"},
      {"type": "li", "segments": [
        ph("ed-eight-years", "8+ years experience",
           ["ev-service-design", "ev-experience-design", "ev-13yrs"])
      ]},
      {"type": "li", "segments": [
        ph("ed-vertical", "Deep industry vertical experience",
           ["ev-wide-industry", "ev-rapid-domain"])
      ]},
      {"type": "li", "segments": [
        ph("ed-enterprise-agency", "Experience in both enterprise and agency worlds",
           ["ev-13yrs", "ev-client-delivery"])
      ]},
      {"type": "li", "segments": [
        ph("ed-it-infrastructure", "Knowledge and experience in IT infrastructure or other technical applications",
           ["ev-tech-stack", "ev-vendor-selection", "ev-enterprise-migration", "ev-ai-product"])
      ]},
      {"type": "li", "segments": [
        ph("ed-social-sciences", "Human behavior, change management, or other applied social sciences",
           ["ev-psych", "ev-change", "ev-coaching"])
      ]},
      {"type": "li", "segments": [
        "Data science, AI/ML background"
      ]},
      {"type": "li", "segments": [
        "You may specialize more deeply in:"
      ]},
      {"type": "li2", "segments": [
        ph("ed-service-design", "Service Design",
           ["ev-service-design", "ev-blueprinting", "pf-global-blueprint"])
      ]},
      {"type": "li2", "segments": [
        ph("ed-ux", "User Experience",
           ["ev-product-leadership", "ev-experience-design", "pf-legacy-ux"])
      ]},
      {"type": "li2", "segments": ["Interface Design"]},
      {"type": "li2", "segments": [
        ph("ed-ia", "Information Architecture",
           ["ev-ia", "pf-eraf"])
      ]},
      {"type": "li2", "segments": ["Graphic Design"]},
      {"type": "li2", "segments": ["Environmental Design"]},
      {"type": "li2", "segments": ["Data Visualization"]},

      {"type": "h2", "text": "Required Education"},
      {"type": "p", "segments": [
        ph("ed-bachelors", "Bachelor’s Degree or equivalent portfolio",
           ["ev-ma", "pf-full"])
      ]},

      {"type": "h2", "text": "Preferred Education"},
      {"type": "p", "segments": [
        ph("ed-masters", "MDM, MDes, MFA, dMBA, or equivalent",
           ["ev-ma", "ev-credentials"])
      ]},
    ]


LEDE = ("These are selected notes and resume points from Ryan Hance's career "
        "experience mapped to the actual Kyndryl job descriptions. Use the tabs "
        "above to switch between the two open roles.")
STAT = "Hover over any underlined phrase and select it to see Ryan's experience related to the ask."
KICKER = "Ryan Hance · Fit Map"
REMOTE = "Fully remote"

data = {
  "meta": {
    "candidate": "Ryan Hance",
    "portfolio": "https://www.hance.work/",
    "note": "Pure renderer input. Edit copy here (or in build_data.py). Each highlighted phrase carries the evidence ids that back it; evidence is a shared dictionary across all roles."
  },
  "roles": [
    {
      "id": "experience-strategist",
      "tab_label": "Senior Experience Strategist",
      "job": {
        "company": "Kyndryl",
        "role": "Senior Experience Strategist",
        "employment": "",
        "location": REMOTE + " · Home office New York, One Vanderbilt · Full time · Req R-64623",
        "url": "https://kyndryl.wd5.myworkdayjobs.com/en-US/KyndrylProfessionalCareers/job/US152580-New-York-US152580-One-Vanderbilt/Senior-Experience-Strategist_R-64623",
        "tab_title": "Ryan Hance · Fit Map",
        "candidate_kicker": KICKER,
        "candidate_lede": LEDE,
        "candidate_stat": STAT,
      },
      "jd_prose": strategist_prose(),
    },
    {
      "id": "experience-designer",
      "tab_label": "Senior Experience Designer",
      "job": {
        "company": "Kyndryl",
        "role": "Senior Experience Designer",
        "employment": "",
        "location": REMOTE + " · Home office Dallas, TX · Full time · Req R-64646",
        "url": "https://kyndryl.wd5.myworkdayjobs.com/en-US/KyndrylProfessionalCareers/job/Dallas-TX-USA/Senior-Experience-Designer_R-64646",
        "tab_title": "Ryan Hance · Fit Map",
        "candidate_kicker": KICKER,
        "candidate_lede": LEDE,
        "candidate_stat": STAT,
      },
      "jd_prose": designer_prose(),
    },
  ],
  "evidence": evidence,
}

out = os.path.join(HERE, "data.json")
with open(out, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# quick self-check: every referenced evidence id exists; phrase ids unique across roles
ids = set()
phrase_ids = []
for role in data["roles"]:
    for b in role["jd_prose"]:
        for seg in b.get("segments", []):
            if isinstance(seg, dict) and "evidence" in seg:
                ids.update(seg["evidence"])
                phrase_ids.append(seg["id"])
missing = [i for i in ids if i not in evidence]
dupes = sorted({p for p in phrase_ids if phrase_ids.count(p) > 1})
print("Wrote", out)
for role in data["roles"]:
    n = sum(1 for b in role["jd_prose"] for s in b.get("segments", []) if isinstance(s, dict) and "id" in s)
    print(f"  {role['id']}: {n} phrases")
print("evidence items:", len(evidence))
print("missing evidence refs:", missing or "none")
print("duplicate phrase ids:", dupes or "none")
unused = [k for k in evidence if k not in ids]
print("unused evidence:", unused or "none")
