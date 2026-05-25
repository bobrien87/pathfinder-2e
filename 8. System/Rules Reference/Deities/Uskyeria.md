---
type: deity
source-type: "Remaster"
domains: "Death, Nature, Vigil, Zeal"
favored-weapon: "Scimitar"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Lose The Path]], Rank 3: [[Cozy Cabin]], Rank 6: [[Nature'S Reprisal]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Whether consciously or not, every successful hunter knows that a balance must be struck between observation and action, preparation and instinct, life and death. Taking more from the land than what is sustainable entices predators to be bolder, possibly turning the hunter into the hunted. Those who seek harmony while they live off the land give deference to Uskyeria, who urges her followers to embrace this equilibrium. Death is a natural part of life. Predators hunt prey. Those who are best suited to do so will survive. Those who don't still feed the circle of life.

**Title** The Saintly Slumberer

**Areas of Concern** Hunting, insomniacs, prudence, slumber

**Edicts** Preserve and protect natural resources, respect the animals you kill and their spirits, sleep as long as you need to in order to have strength for the day

**Anathema** Kill animals for reasons other than self-defense or sustenance, over-hunt the land, prevent others from getting as much sleep as they want

**Religious Symbol** crossed scimitars

**Sacred Animal** bear

**Sacred Colors** brown, red

**Source:** `= this.source` (`= this.source-type`)
