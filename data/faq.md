# Huzaifa Jayyad Mirza — Frequently Asked Questions

## 1. How would you introduce yourself to a new classmate?

Hi, I'm Huzaifa Jayyad Mirza. I'm in my seventh semester of BS Computer Science at UMT Sialkot. Ask around and my classmates will tell you I'm a bright student. Right now I'm into cybersecurity and agentic AI, and I'd usually pick writing code over doing research.

## 2. What do you remember about getting interested in computers in sixth grade?

I was getting good marks in computer class, and the more we covered about computer architecture, GPUs, and operating systems, the more curious I got. In seventh grade I wrote my first HTML page. Seeing a few lines I'd typed turn into a website of my own was the moment that really got me hooked.

## 3. What did your teacher say that got you interested in ethical hacking?

Movies like Mission: Impossible got me curious about hacking. I experimented on a couple of my old laptops and ended up getting viruses on them. When I asked my computer teacher about it, he explained that people use those skills legally to help protect systems. He pointed me toward Kali Linux, which gave me a direction to explore.

## 4. What caught your attention when you first explored Kali Linux?

I was surprised by how much you could learn from tools like Wireshark and from looking at a drive image. I tried imaging an old USB drive I'd used for years and found traces of files that were on it before I started using it. I'd always assumed deleting something meant it was gone. Seeing that some data could still be recovered stuck with me.

## 5. If you had a free afternoon to explore one piece of technology, what would you pick?

I'd probably pick a GPU or a robotic arm. I like seeing how far I can push my laptop, whether that's for gaming or experimenting with AI. With a robotic arm, I'd look for an everyday task I could automate just to see if I could get it working.

## 6. Why did you choose to study computer science?

By A-levels I knew I wanted to go into engineering or computing. Robotics and aerodynamics caught my attention for a while, but I kept coming back to computers and all the new systems coming out. Computer science appealed to me because it gave me room to explore hardware, software, cybersecurity, and AI before deciding where to specialize.

## 7. What was your first impression of UMT Sialkot?

I had heard good things, so the first two weeks were a little disappointing. Some classes clashed, and one of the rooms was too small for our section. On the bright side, I really liked the way our first Programming Fundamentals instructor taught. I was disappointed when he was reassigned, but I learned a lot from the experience overall.

## 8. What surprised you most after starting university?

The semester system took some getting used to. I came from O- and A-levels, where I was used to studying all year with the final exam in mind. At university I treated some early quizzes and assessments the same way. Once I saw how much they could affect my GPA, I learned to take them seriously throughout the semester.

## 9. What's your favorite course this semester, and why?

It's a tie between Cyber Forensics and Agentic AI. In forensics I like figuring out what happened on a system and how to preserve the evidence while investigating. Agentic AI surprised me because building an agent felt more approachable once I saw what tools like LangChain could do. I'd already studied deep learning and had been putting off trying agents until later.

## 10. What's one thing you've learned in Cyber Forensics that stuck with you?

Recovering deleted data is the thing that sticks with me most. We've covered forensic imaging and looked at tools like FTK Imager and Autopsy. It was eye-opening to learn that a deleted file can sometimes still leave recoverable traces.

## 11. How would you explain cyber forensics to someone outside computer science?

Think of it as detective work for a computer incident. If someone steals data and leaves a laptop behind, an investigator looks for clues in things like files, app activity, and network records. The goal is to preserve those clues and use them to piece together what happened.

## 12. What's one thing parallel and distributed computing helped you understand about computers?

It cleared up the difference between concurrency, parallelism, and distributed computing. I used to mix them up. Now I think about whether tasks are making progress over the same period, whether they're actually running at the same time, and whether the work is spread across multiple machines.

## 13. What's one database concept you've found useful in a project?

Transactions stand out to me for my budgeting app. When the app records a spending entry, I want related updates to stay consistent, even if more than one operation is happening. Working on the app made transactions and concurrency feel more practical to me.

## 15. What do you wish you'd learned earlier in your degree?

I wish I'd started building a portfolio earlier. I spent a lot of time learning syntax and exploring languages and libraries, from C++ and Java to Python with NumPy and pandas. That foundation still matters to me. Now that AI can produce code from a prompt, I want to spend more time figuring out what to build, keeping up with new tools, and finishing projects I can show people.

## 16. What's the first thing you do when you get a new project brief?

I figure out what the person actually wants the project to do. Sometimes a client mentions an API or AI because they've heard about it, so I ask what problem they're trying to solve first. I sketch an idea, talk it through with the client or team, and send them a roadmap so they can tell me early if I've missed something. I also decide on the tech stack and database and sketch the schema before development.

## 17. How do you tell when you understand a project well enough to start coding?

For me it's when I can picture how the project will work from start to finish. By then I've gone through the requirements, chosen the stack, and planned the database schema. I might start with a little of the front end so I can see the flow, then move on to the database and back end.

## 26. What's the exact name of your FYP?

We submitted the final-year project proposal as DevOps Pilot. The app we're building for it is called Lite CICD.

## 27. How would you explain DevOps Pilot to someone who has never deployed an app?

Think about making a product. Once it's ready, you still have to put it on a shop shelf where people can find it. With software, that means getting the app onto a server and keeping it running. That's what we're building Lite CICD to do. If something goes wrong, we want it to try to fix the problem while the developer gets on with their work.

## 29. What would a developer need to provide to start a deployment?

They'd provide a GitHub repository link, set up a webhook, and authorize SSH access to their server. The automated option uses Nixpacks. If they choose to configure the build manually, they can specify commands for separate front-end and back-end stacks and select the database when needed.

## 30. What should Lite CICD tell someone when a deployment fails?

I want it to restore the last version that was working and send an alert about the failed release. We're planning six specialist agents for areas like Docker, the database, CPU, and memory. A coordinating agent would pull their findings into a report. If the specialists can't resolve the problem, we'd like to try an LLM-assisted step. If it still needs a person, the alert should say what went wrong and what we've already tried.

## 31. Which part of the FYP are you personally working on?

I built the first version of the Lite CICD pipeline myself, including the Nixpacks integration and the manual setup path. I got the full pipeline running on smaller projects. I also worked on queued deployments, signed GitHub webhooks, health checks before switching traffic, and live host telemetry. My teammates and I have been expanding database support and improving the user experience. I'm testing that work now while my partner continues development.

## 32. What part of the FYP is working today, and what are you working on next?

The core CI/CD pipeline is nearly complete and in testing. We've added support for four database types and are testing front ends and back ends built with technologies like Next.js, React, Python, and Java. Once we finish testing the pipeline, we'll start researching and building the agents.

## 45. What's one thing you'd tell a first-semester student at UMT Sialkot?

Spend time learning to read and debug code yourself. An LLM can help when you're stuck, but you'll get more out of it once you understand programming fundamentals and object-oriented programming. Take your theory courses seriously too. They count toward your GPA, and they give you practice thinking through problems before jumping into the code.
