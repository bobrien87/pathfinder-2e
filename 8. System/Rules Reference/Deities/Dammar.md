---
type: deity
source-type: "Remaster"
domains: "Healing, Indulgence, Luck, Soul"
favored-weapon: "Shortsword"
divine-font: "Heal"
divine-skill: "Medicine"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In the Age of Creation, the first time a soul was plucked from the River of Souls and returned to life, a psychopomp usher of life and resurrection emerged. Dammar the Denied is that first piece of resurrection magic made manifest, the psychopomp usher of life and journeys back from the Boneyard, and they ensure mortals don't make that journey too often or too easily. Alongside souls returning from the grave, Dammar presides over medicine, doctors who stave off death before it even arrives, alcohol (particularly, though not exclusively, used in medical preparations), and the unyielding tenacity of cockroaches and other insects who look upon death and refuse.

**Title** The Denied

**Areas of Concern** Liquor, luck, medicine

**Edicts** Respect the cycle of souls, heal the sick and injured, experience a hangover after drinking

**Anathema** Create undead, waste medicines instead of using them, harm an innocent insect

**Religious Symbol** one horizontal line crossed by two vertical lines, surrounded by four dots

**Sacred Animal** cockroach

**Sacred Colors** brown

**Source:** `= this.source` (`= this.source-type`)
