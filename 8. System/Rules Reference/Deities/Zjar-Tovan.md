---
type: deity
source-type: "Remaster"
domains: "Metal, Might, Introspection, Zeal"
favored-weapon: "Greatsword"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Ghostly Weapon]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Zjar-Tovan is a name few are familiar with, as those who worship the Bladesoul are often mistaken for devotees of a god of the forge, such as Torag, or champions of a mighty military god, such as Iomedae. But to Zjar-Tovan, a weapon is more than just a tool. It is a statement against restriction or captivity, and a method to impart one's will against those who would resist embracing freedom of self-expression. To use a weapon is to make a choice, and as a sentient and living apparatus of war, Zjar-Tovan blesses those who use their tools with conviction, no matter their actions or cause.

**Title** The Bladesoul

**Areas of Concern** armaments, motivation, self-expression

**Edicts** aid those who cannot freely live as they would choose to, do not allow your purpose to be overly guided by another's will, inspire others with your personal convictions

**Anathema** belittle an ally (or someone you respect) when they express their beliefs, serve a cause you do not truly believe in

**Religious Symbol** half-finished sword resting on an anvil

**Sacred Animal** none

**Sacred Colors** blue, gray, silver

**Source:** `= this.source` (`= this.source-type`)
