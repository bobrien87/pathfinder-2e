---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Healing, Wyrmkin"
favored-weapon: "Maul"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Fleet Step]], Rank 3: [[Haste]], Rank 6: [[Dragon Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The god Uvuko dances across the land, his body forming the boundary between earth and sky. His twisting tail churns the air into clouds, his creations spreading water to all those who thirst. His sliding scales till the earth, bringing forth plants that are nourished by Uvuko's rains. The worship of Uvuko is widespread in the Mwangi Expanse, found among many lizardfolk tribes, Mbe'ke and Taralu dwarves, and in the more cosmopolitan cities.

**Title** The Diamond Ring

**Areas of Concern** Metamorphosis, cycles, growth, fertility

**Edicts** Embrace change and the future, master adversity with flexibility, foster freedom and progress for others

**Anathema** Allow yourself and your surroundings to stagnate, crush an egg, use vile or cruel language

**Religious Symbol** serpent curled in a ring

**Sacred Animal** swift

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
