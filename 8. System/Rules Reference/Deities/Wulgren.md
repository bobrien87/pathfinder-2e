---
type: deity
source-type: "Remaster"
domains: "Ambition, Creation, Freedom, Perfection"
favored-weapon: "Barricade-buster"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Sure Strike]], Rank 4: [[Creation]], Rank 6: [[Phantasmal Calamity]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Wulgren, like Jukha, is a dromaar. He traveled exceptionally far and wide as a mortal before his ascension. Wulgren was born in Belkzen but became separated from his party during a scouting expedition. After a brief period held captive by a group of adventuring Pathfinders, Wulgren was freed on his own recognizance and traveled to Alkenstar, the City of Smog.

While in Alkenstar, Wulgren developed a great skill in weapon smithing and forged an unlikely and powerful firearm: the barricade buster. With this massive, inaccurate, but deadly weapon in hand, Wulgren swore his Deathright and returned to Belkzen to stand against the hordes of the Whispering Tyrant. During a brutal battle against an endless stream of skeletal undead, Wulgren and his mighty weapon ultimately fell, and he continued on to fight his Crucible.

It's unclear which orc deity Wulgren slew; most likely it was another orc who had passed the Crucible previously, whose name had not yet spread widely enough to be well known. Whoever they were, Wulgren defeated them (though it's unclear if he did so with his barricade buster or more conventional weaponry), and Wulgren the Bone-Breaker now stands proudly among Belkzen's gods.

**Title** The Bone Breaker

**Areas of Concern** Destruction of undead, firearms, invention

**Edicts** Create the weapons you intend to wield with your own two hands, innovate efficient ways to defeat your enemies

**Anathema** Wield a weapon forged by another except in direst circumstance, yield ground to an enemy while victory is still possible

**Religious Symbol** hammer striking a bone

**Sacred Animal** boar

**Sacred Colors** gray, white

**Source:** `= this.source` (`= this.source-type`)
