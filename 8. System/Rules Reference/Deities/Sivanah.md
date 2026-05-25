---
type: deity
source-type: "Remaster"
domains: "Delirium, Magic, Secrecy, Trickery"
favored-weapon: "Bladed-scarf"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 2: [[Blur]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

No ancient record reveals the truth of Sivanah's origins; in fact, only recent documents record her existence at all. The Seventh Veil is widely regarded as the goddess of illusion magic, often portrayed as a figure disguised by seven veils. Legends state that each face underneath the first six of her seven veils is of a different ancestry—human, elf, halfling, gnome, anadi, and naga—but the seventh face is never shown, believed to mask the goddess's true form. Some theologians believe Sivanah hails from the Netherworld, though the goddess's true nature and form continue to be topics of debate. Even her female visage, while agreed upon by her followers, could likewise be an illusion. Her goals are hidden from even her most faithful, which some believe has hampered the faith's growth and influence beyond the level of a cult.

**Title** The Seventh Veil

**Areas of Concern** illusions, mysteries, reflections, secrets

**Edicts** show the beauty in illusions, pursue the nature of truth, respect the need for secrets

**Anathema** let a creature permanently labor under the falsehood of your illusions, reveal a secret you have sworn to keep

**Religious Symbol** veils tied in circle

**Sacred Animal** coyote

**Sacred Color** gray

**Source:** `= this.source` (`= this.source-type`)
