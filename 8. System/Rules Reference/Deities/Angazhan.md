---
type: deity
source-type: "Remaster"
domains: "Destruction, Might, Nature, Tyranny"
favored-weapon: "Fist, Spear"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Animal Form]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Angazhan is a name well known in the Mwangi Expanse, and for good reason. Called the Ravenous King and Demon Lord of Beasts, he appears as an enormous and terrifying red-furred ape with six long fingers on each hand, massive and clawed. His red eyes, twisted horns, and viciously sharp fangs give him a demonic appearance. His followers range from gnolls to charau-kas to nalfeshnee demons that number in the thousands.

Angazhan has astounding presence and influence, but that influence is rivaled by his raw power. He is skilled enough with weapons, but prefers to use his own abilities-his powerful fists, lethal fangs, sharp horns, and deadly tail. His terrible grasp extends beyond life into death, as well. Occasionally, those slain in combat by Angazhan's minions are reincarnated forcefully into an ape-like creature in the service of the Ravenous King. This curse causes the victim to serve eternally, and only upon death is there a chance for their soul to be retrieved before it slips into the Boneyard, to be sent on and suffer a never-ending torment in the Abyss.

**Title** The Ravenous King

**Areas of Concern** Apes, jungles, tyrants

**Edicts** Commit acts of brutal violence, test yourself against nature, make animals more dangerous

**Anathema** Cower from fights, allow yourself to be resurrected instead of reincarnated

**Religious Symbol** Demonic ape face

**Sacred Animal** Ape

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
