---
type: deity
source-type: "Remaster"
domains: "Creation, Healing, Knowledge, Metal"
favored-weapon: "Falcata"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Object Reading]], Rank 2: [[Animated Assault]], Rank 7: [[Contingency]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When the behemoth Ousmariku ravaged western Iblydos, the hero-god Ximakter drew his curved blade and led a band of other mythic warriors against the beast. Ousmariku consumed Ximakter, sending his sword flying to lodge into the nearby beach. Within days of being recovered, the blade awoke with magical intelligence and mythic power. Recognizing this as a novel hero-god, Iblydans swiftly constructed a temple-armory for the divine blade. Known as Aerekostes, the sword has never confirmed the origin of its personality, be it the trapped soul of Ximakter or some spontaneously created entity.

Aerekostes doesn't just lend magical power; they lend themselves. Aspiring heroes can petition the sword for help, and Aerekostes occasionally agrees to accompany them for some worthy quest. However, if the quest goes awry, the sword sometimes disappears for weeks or even years before resurfacing.

**Title** The Mentor in Blades

**Areas of Concern** contingencies and intelligent items

**Edicts** make items, treat items well, prepare for many possibilities

**Anathema** destroy an intelligent item

**Religious Symbol** kopis encircled by mystical runes

**Sacred Animal** lungfish

**Sacred Colors** blue and bronze

**Source:** `= this.source` (`= this.source-type`)
