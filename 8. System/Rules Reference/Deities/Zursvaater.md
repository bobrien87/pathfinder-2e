---
type: deity
source-type: "Remaster"
domains: "Fire, Trickery, Tyranny, Zeal"
favored-weapon: "Greatsword"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 3: [[Blazing Dive]], Rank 5: [[Elemental Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Zursvaater is considered the patron deity of fire giants. According to legend, well over ten millennia ago, a stone giant clan was scaling the rocky face of the mightiest volcano on Golarion, once known as the Molten Summit. He took on a new form to better communicate with them, molding the mountain range that was his body into a colossal humanoid figure of volcanic rock and ash. In this form, he called himself Zursvaater and offered the clan the secrets of fire and metal in exchange for their complete devotion and their very souls. Upon accepting, they were subsumed by the god before being expelled as beings of molten rock and flame—the first fire giants.

**Title** Prince of Steel

**Areas of Concern** Conquest, metal crafting, tactics

**Edicts** Conquer the weak, devise plans ahead of anticipated battles, only bring well-maintained weapons to fights

**Anathema** Engage in violent infighting, claim anyone but Zursvaater gives you your strength, disrespect a skilled smith

**Religious Symbol** helm with huge fangs

**Sacred Animal** saber-toothed tiger

**Sacred Colors** black, orange

**Source:** `= this.source` (`= this.source-type`)
