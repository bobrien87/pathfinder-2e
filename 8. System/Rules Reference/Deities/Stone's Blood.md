---
type: deity
source-type: "Remaster"
domains: "Creation, Family, Protection, Wealth"
favored-weapon: "Warhammer"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Ant Haul]], Rank 4: [[Creation]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Many dwarves choose to venerate the entire pantheon of dwarven gods as one, colloquially known as Stone's Blood. These deities function as a family unit, with Torag as the patriarch. They get along as well as any family might, disagreeing on many matters but always cooperating for the good of the whole. Worship of Stone's Blood includes all aspects of dwarven life, and devotees are among the strongest pillars of any dwarven community.

**Pantheon Members** Angradd, Bolka, Dranngvit, Droskar, Folgrit, Grundinnar, Kols, Magrim, Torag, Trudd

**Areas of Concern** ancestry, crafting, dwarves, relationships

**Edicts** develop skills useful to your community (especially crafting, mining, and trading), honor your ancestors through tradition and rituals

**Anathema** dishonor your family, irreparably damage an ancestral relic, willingly break a contract or oath

**Religious Symbol** dwarven anvil

**Source:** `= this.source` (`= this.source-type`)
