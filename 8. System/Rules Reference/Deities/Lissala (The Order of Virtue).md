---
type: deity
source-type: "Remaster"
domains: "Ambition, Duty, Fate, Knowledge"
favored-weapon: "Whip"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Mindlink]], Rank 2: [[Animus Mine]], Rank 6: [[Never Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Lissala, the Order of Virtue, has changed drastically from the times of ancient Azlant. Her teachings created the foundation of the Seven Virtues of Rule, later adopted by the realm of Thassilon. While those seven virtues held aspects of charity, humility, and love, Lissala encouraged her followers to focus more prominently on teachings of duty and strict adherence to her guidelines. She believed, and taught, that those who followed her teachings would be greatly rewarded.

**Title** The Order of Virtue

**Areas of Concern** Duty, fate, rewards for service, runes

**Edicts** Gather and share knowledge freely, honor your duty when your word is given, respect and carry out the law

**Anathema** Conceal and keep information secret, break an oath, subvert authority

**Religious Symbol** sihedron

**Sacred Animal** snake

**Sacred Colors** gold and green

**Source:** `= this.source` (`= this.source-type`)
