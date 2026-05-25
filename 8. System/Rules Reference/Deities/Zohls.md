---
type: deity
source-type: "Remaster"
domains: "Ambition, Cities, Knowledge, Truth"
favored-weapon: "Heavy-crossbow"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Share Lore]], Rank 3: [[Hypercognition]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Zohls, also known as Verity, advocates for determination, investigation, and truth. She believes that mysteries lead to truth, but how one arrives at that truth is as important as the answer itself. All questions are puzzles, and all puzzles are worth solving. The more intricate the problem, the more rewarding the investigation, and through determination and ethical investigation, even the deepest of enigmas can be solved. Calculated, logical thinking is more important to Zohls than gut instinct. She sees patterns everywhere, and she teaches that detecting these patterns brings the truth to light. While all investigations are worth pursuing so long as they don't hurt innocents, investigations that reveal the truth of crimes or other horrors, and that lead to justice being served and victims finding peace, are the most important of all to Verity.

**Title** Verity

**Areas of Concern** Determination, investigation, truth

**Edicts** Solve logic puzzles, investigate crimes, devise new solutions from research

**Anathema** Make judgments without evidence, contaminate evidence, obstruct truths

**Religious Symbol** Book with chequered page

**Sacred Animal** wren

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
