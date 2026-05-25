---
type: deity
source-type: "Remaster"
domains: "Confidence, Duty, Might, Protection"
favored-weapon: "Warhammer"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Endure]], Rank 3: [[Haste]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In crafting Trudd as a gift for his beloved, Torag thought of the qualities he'd not given his other children. After a few moments of contemplation, he settled on the simplest and most elusive answer—he had not gifted his wife with a child who bore the strength of the mountains themselves. He was to be his father's strong left hand, acting as the general of Torag's armies when defending Heaven from incursions by demons or other such nefarious forces. Trudd's personal charge was to guard the seat of Forgeheart when the Father of Creation traveled the multiverse. Trudd took to these dual tasks with glee and has been doing his duty ever since.

Trudd is almost unknown outside of dwarven halls, or at least he once was. When the Whispering Tyrant broke free, dwarven Knights of Lastwall began to share his teachings with their fellow knights and compatriots. Trudd's religion is spreading slowly but steadily among humans, half-elves, and even orcs. Trudd doesn't know what to make of this, but overall, he is doing his best to respect his new followers, accepting these new children as a loving adoptive father. He sends omens of warning if a vulnerable target is about to be attacked and blessings of endurance to keep guards awake and on task. In Trudd's mind, almost nothing is as important as guarding his followers and his followers guarding their own charges.

**Title** The Mighty

**Areas of Concern** Bravery, defense, strength

**Edicts** Offer your strength to aid others, protect those weaker than you

**Anathema** Engage in petty demonstrations of strength, use your strength to take advantage of others

**Religious Symbol** warhammer in front of a golden shield

**Sacred Animal** bear

**Sacred Colors** brown, gray

**Source:** `= this.source` (`= this.source-type`)
