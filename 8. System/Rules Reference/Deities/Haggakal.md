---
type: deity
source-type: "Remaster"
domains: "Darkness, Nightmares, Trickery, Zeal"
favored-weapon: "Greatclub"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Endure]], Rank 3: [[Shift Blame]], Rank 5: [[Aberrant Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Haggakal is an ogre god, the offspring of a profane deity and a giant, the names of which have been either lost or intentionally scrubbed from the annals of time and even Bergelmir's tome, likely by the very beings who owned them. His hideous appearance is emphasized in all sorts of tales about him, regardless of whether the goal of the stories were to praise or disparage him. He is known as the god of ogres, darkness, illicit relationships and illicit deals among the few giants and even fewer ogres who worship him. His followers likewise become more unsightly the longer and more fervently they revere him. The only traits of Haggakal that are highlighted more than his unpleasant looks are his unholy strength and incredible cunning.

**Title** Father Moon

**Areas of Concern** Darkness, ogres, temptation

**Edicts** Always accept a challenge of strength, facilitate chaos and instability

**Anathema** Flee from battle, get married, hide the ugly features bestowed onto you by Haggakal

**Religious Symbol** leering ogre face

**Sacred Animal** boar

**Sacred Colors** tan, white

**Source:** `= this.source` (`= this.source-type`)
