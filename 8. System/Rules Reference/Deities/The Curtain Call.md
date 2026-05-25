---
type: deity
source-type: "Remaster"
domains: "Creation, Family, Indulgence, Passion"
favored-weapon: "Sword-cane"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 3: [[Enthrall]], Rank 5: [[Illusory Scene]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The deities associated with this pantheon are [[Arshea]], [[Bolka]], [[Findeladlara]], [[Nocticula]], and [[Shelyn]].

**Areas of Concern** acting, directing, orchestral music, set building

**Edicts** help to create public works of art, encourage creativity in others, fight against propaganda and weaponized art meant to spread harm, support fellow creatives as you would your own family

**Anathema** censor or destroy legitimate works of art, leave those who depend on you to fend for themselves at the last minute, use phrases like "good luck" that might tempt the fickle forces of fate to ensure the opposite comes to pass

**Source:** `= this.source` (`= this.source-type`)
