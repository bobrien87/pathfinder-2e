---
type: deity
source-type: "Remaster"
domains: "Dragon, Destruction, Fire, Zeal"
favored-weapon: "Jaws, Whip"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 3: [[Fireball]], Rank 5: [[Summon Dragon]], Rank 9: [[Implosion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Dahak was the first child of the draconic divinities Apsu and Sarshallatu. His parents thought he would help them be architects of the creation of the mortal world, but instead he sought destruction. It isn't clear why Dahak fostered such hatred for creation in his heart, but whenever Apsu, Sarshallatu, and Dahak's siblings built something, Dahak would appear to attempt to destroy it. Soon, this led to an outright war between Dahak and his family, one in which the Endless Destruction was almost struck down. However, his mother prevented Apsu from dealing a fatal blow, and Dahak fled to Hell to regain his strength.

Since then, Dahak has become a patron for hateful dragons and those who want to jealously destroy everything they cannot possess. He began to focus on finding a way to siege his father's divine realm to finish their fight. However, when Dahak learned that many of Golarion's deities were joining forces to imprison Rovagug, the dragon decided not to take advantage of the chaos to kill Apsu. Instead, he spoke with his progenitor to issue a decree: the final battle between them would eventually take place on Golarion, much to Apsu's chagrin. Dahak now builds his power for that fateful day when he and his draconic followers take their rightful place as the rulers of the world (as destroyed as it might be after a massive battle between Apsu and Dahak).

**Title** The Endless Destruction

**Areas of Concern** destruction, greed, wicked dragons

**Edicts** kill dragons, destroy things at your whim, study past disasters

**Anathema** spare a foe after you have chosen to kill them, forgive a slight, prevent the destruction of things that cannot be saved

**Religious Symbol** falling, burning scale

**Sacred Animal** none

**Sacred Colors** black, red, white

**Source:** `= this.source` (`= this.source-type`)
