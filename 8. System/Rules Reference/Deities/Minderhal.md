---
type: deity
source-type: "Remaster"
domains: "Creation, Duty, Earth, Might"
favored-weapon: "Warhammer"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Summon Construct]], Rank 3: [[Ghostly Weapon]], Rank 4: [[Replicate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Minderhal is both praised and scorned for his inflexibility and dedication to the status quo. The stone giant god of creation, giants, justice, and strength has a dwindling following, partially due to modern stone giants preferring to pay homage to the spirits of their ancestors over any gods. He instilled the belief that it is more honorable to exile yourself from a clan than to challenge superiors or existing traditions. Minderhal even went as far as encouraging the stone giants to accept being enslaved by the Thassilonians in exchange for political and magical might for himself, citing that it was only natural for the strong to subjugate the weak. Unsurprisingly, the moment the Thassilonian empire crumbled, so did faith in him.

**Title** He Who Makes and Unmakes

**Areas of Concern** Creation, giants, justice, strength

**Edicts** Strictly follow established tradition, conquer the weak, obey those in power

**Anathema** Break tradition, question those with greater positional power, provide succor to those who have turned their backs on Minderhal

**Religious Symbol** anvil in triangle

**Sacred Animal** cave bear

**Sacred Colors** brown, gray

**Source:** `= this.source` (`= this.source-type`)
