---
type: deity
source-type: "Remaster"
domains: "Air, Dust, Freedom, Travel"
favored-weapon: "Longbow"
divine-font: "Harm, Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 3: [[Wall Of Wind]], Rank 8: [[Punishing Winds]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Plane of Air is a vast expanse of open sky dotted with the occasional floating island, flying creature, or airborne vessel. Though, like all elemental planes, it is home to its own deities, some might offer their worship to the plane itself and its many elemental creatures. Those who follow this covenant celebrate clean air, fresh breezes, and strong winds, believing they can blow away both physical and spiritual impurities. They tend to be those who have naturally evolved the power of flight or who can take to the sky using magic or personal technology. However, those who build big smoke-belching flying vessels are usually seen as adversaries to those devoted to the Breath of the Endless Sky and might find themselves fending off angry saboteurs who seek to bring their contraptions back down to earth.

**Covenant Members** air elementals, anemoi, jaathooms, the Plane of Air, spirits of air

**Areas of Concern** breath, clean air, clouds, flying, winds

**Edicts** respect creatures capable of natural flight, revel in the glory of flight, stop to feel breezes across your body when possible

**Anathema** pollute the air with excessive smoke or chemicals, suffocate a living creature

**Religious Symbol** gusting breeze

**Source:** `= this.source` (`= this.source-type`)
