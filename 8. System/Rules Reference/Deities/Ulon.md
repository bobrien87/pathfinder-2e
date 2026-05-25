---
type: deity
source-type: "Remaster"
domains: "Knowledge, Secrecy, Trickery, Truth"
favored-weapon: "Crossbow"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 2: [[Paranoia]], Rank 4: [[Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ulon is one of the most mysterious gods from ancient Azlant society. A god of conspiracy, isolation, and manipulation, Ulon believed that uncovering truths and sowing mistrust and questions that distracted society from the on-going underground machinations of the Web. Knowing that truth and lies are often found in the same vein, Ulon encouraged picking apart lies to reveal the truth beneath them, pushing followers toward a greater concept known as the All-Truth.

**Title** The Web

**Areas of Concern** Conspiracy, isolation, manipulation

**Edicts** Discover and unravel the hidden truths, motivate others to fight and question each other, keep secrets close to the chest

**Anathema** Blindly accept what you're told, share the All-Truth, support or promote unjustified hierarchy

**Religious Symbol** black pentagon within a purple circle

**Sacred Animal** spider

**Sacred Colors** black and purple

**Source:** `= this.source` (`= this.source-type`)
