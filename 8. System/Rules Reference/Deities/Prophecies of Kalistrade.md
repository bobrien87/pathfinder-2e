---
type: deity
source-type: "Remaster"
divine-skill: "Diplomacy"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The secular prophecies of Kalistrade are famously centered on a single principle: amassing personal wealth both in search of and as evidence of personal enlightenment. The prophets of Kalistrade, often referred to as Kalistocrats, believe that achieving purity of body, mind, and spirit will lead to financial success, and thus they avoid certain foods and eschew contact with most persons and objects as impure. To avoid contamination and contact with nonbelievers they wear long, white gloves, and they wear distinctive, all-white clothing to represent their purity-often incorporating their symbol, a circle inside a triangle that is itself inscribed in a larger circle.

**Areas of Concern** trade, wealth, self-denial, stability

**Edicts** accumulate personal wealth, seek enlightenment through purity of self, foster and aid mercantile pursuits, welcome newcomers regardless of gender or ancestry

**Anathema** spend money frivolously; offer money to those who don't deserve wealth; overindulge in physical pleasures, food, or drink; give charity to others

**Source:** `= this.source` (`= this.source-type`)
