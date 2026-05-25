---
type: deity
source-type: "Remaster"
domains: "Destruction, Dust, Fire, Sun"
favored-weapon: "Mace"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 2: [[Floating Flame]], Rank 3: [[Cup Of Dust]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Nurgal, the Shining Scourge, is the demon lord of deserts, senseless warfare, and the sun. He was formerly a fully fledged deity of ancient Azlant, but fell to demigodhood after being defeated in combat. Nurgal represents the sun's potential for devastation, and his followers venerate him out of cowed awe. The demon lord appears as a muscular, tanned man with the head and lower body of a golden lion and a dragon's tail. He is almost always depicted as wielding a mace in the form of a miniature sun, held in a taloned hand. Nurgal's worshippers are primarily found in the deserts of Garund, Ninshabur, and Qadira.

**Title** The Shining Scourge

**Areas of Concern** Deserts, senseless warfare, the sun

**Edicts** Wage war in the desert, deny water to your foes

**Anathema** Heal a sunburn, change your name

**Religious Symbol** lion jaws around the sun

**Sacred Animal** lion

**Sacred Colors** yellow, orange

**Source:** `= this.source` (`= this.source-type`)
