---
type: deity
source-type: "Remaster"
domains: "Change, Disorientation, Luck, Trickery"
favored-weapon: "Gnome-flickmace"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Befuddle]], Rank 3: [[Hypnotize]], Rank 6: [[Vibrant Pattern]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Some people just want to throw the world into chaos, whether on a smaller scale through vexing pranks or on a larger scale by embracing complete anarchy. Adherents to the Pandemonia venerate the most confounding of extraplanar entities, ones who refuse to be bound by order and decorum to do whatever they want whenever they want. Some claim that their acts are all in good fun, but they often don't take the feelings of those they trick into account. Others know full well the consequences of their actions and simply don't care who they hurt. As befitting such a chaotic covenant, there is hardly any conformity of beliefs or methods within its ranks, making it almost more of a philosophy (albeit a rather disorganized one) than anything else.

**Covenant Members** mischievous fey, protean shapers, shapechanging spirits

**Areas of Concern** chaos, confusion, metamorphoses, pranksters

**Edicts** disrupt the status quo, never given reasons for your actions, play elaborate tricks on the unsuspecting

**Anathema** fall into a set routine, fix something that you have broken

**Religious Symbol** messy swirl of colors

**Source:** `= this.source` (`= this.source-type`)
