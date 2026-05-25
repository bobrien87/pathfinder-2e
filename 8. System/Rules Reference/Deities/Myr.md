---
type: deity
source-type: "Remaster"
domains: "Ambition, Family, Duty, Perfection"
favored-weapon: "Longsword"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Mountain Resilience]], Rank 6: [[Nature'S Reprisal]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Myr, the Guide of Perfection, believed in honoring the past and respecting the wishes of the ancestors to follow an individual path forward. She taught that doing good deeds and living a charitable life honors those that came before and promotes a value in all life. While she promoted perfecting one's body, it wasn't her most significant edict. As society in Azlant prospered and grew, however, some took Myr's teachings at face value. They prayed to Myr for aid in physical perfection and ignored the values of her other teachings. This made Myr an unconventional, but popular, goddess for warriors and athletes.

**Title** The Guide of Perfection

**Areas of Concern** Charity, lineage, physical perfection

**Edicts** Strive for perfection in mind and body, respect and honor those who came before you, use your means to aid the less fortunate

**Anathema** Take life needlessly, take from those less fortunate, ignore someone in need

**Religious Symbol** branching tree and roots

**Sacred Animal** dove

**Sacred Colors** purple

**Source:** `= this.source` (`= this.source-type`)
