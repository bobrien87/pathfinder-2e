---
type: deity
source-type: "Remaster"
domains: "Change, Knowledge, Perfection, Zeal"
favored-weapon: "Bladed-gauntlet"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Hypercognition]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Will the thunder of battle drums make your heart race or your knees quake? Could you stand firm in the face of an enemy charge? These are questions that all warriors must confront, and many call for Genzaeri's favor when they do. As a goddess of battlefield tactics and innovation, Genzaeri sees the field of combat as the ultimate classroom, teaching strategy, tactics, and weapons. Equally blessed by Genzaeri is the historian knowledgeable in enemy weaknesses, the inventor developing a deadly prototype, and the corporal who gives her first command.

The goddess encourages her followers to use combat as the means to learn about themselves and the world around them. The field is the best place to test new fighting techniques and weapons of war, of course, but Genzaeri's followers consider a good fight the opportunity to test their mettle and find out how to adapt themselves to new challenges. After a fight, worshippers reflect on what they learned and see how any new knowledge might be adopted into life outside of combat. Whether they bring useful alchemical concoctions, weapons that double as effective tools, or hard-won personal truths, Genzaeri's followers innovate their lives and communities.

**Title** The Telling Trial

**Areas of Concern** battlefields, modernization, negotiation, and tactics

**Edicts** develop and use the appropriate tool for the job, share plans with allies, use conflict to demonstrate the best in yourself

**Anathema** avoid a winnable conflict, retry a failed tactic in the same engagement

**Religious Symbol** crucible pouring molten metal

**Favored Animal** magpie

**Favored Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
