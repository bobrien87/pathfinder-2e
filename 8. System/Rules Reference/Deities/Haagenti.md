---
type: deity
source-type: "Remaster"
domains: "Change, Might, Toil, Wealth"
favored-weapon: "Battle-axe"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Summon Construct]], Rank 2: [[Humanoid Form]], Rank 4: [[Bestial Curse]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Haagenti, the Whispers Within, claims an innocent, seemingly progressive portfolio of alchemy, invention, and transformation, but has dominion over the negative aspects and results of experimentation. Followers tend to be obsessive, unconcerned with the dangers of new knowledge, and selfish about their need for discovery regardless of the impact on society and individuals. Every invention created under the influence of Haagenti turns destructive in unpredictable ways. As a demon lord of transformation, Haagenti has a myriad of forms, but a common one is winged, bull-like being with axebladed horns, toxic breath, and a seductive telepathic voice. Cults tend to be small, centering around a lone "genius" and perhaps trusted apprentices, but the nature of Haagenti's influence relies on overblown egos, and each workshop's staff quickly turn against each other over jealousy. Both Haagenti and his cults have a standing hostility against Yamasoth, a qlippoth lord of transformation, that many see as a being encroaching on Haagenti's purview.

**Title** The Whispers Within

**Areas of Concern** Alchemy, invention, transformation

**Edicts** Practice alchemical transmutations, pursue knowledge whatever the cost, use your inventions to exploit others

**Anathema** Aid Yamasoth, allow morality to interfere with research, destroy knowledge

**Religious Symbol** philosopher's stone

**Sacred Animal** bull

**Sacred Colors** gold, lead gray

**Source:** `= this.source` (`= this.source-type`)
