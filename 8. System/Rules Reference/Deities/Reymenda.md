---
type: deity
source-type: "Remaster"
domains: "Duty, Repose, Toil, Zeal"
favored-weapon: "Falchion"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Tailwind]], Rank 4: [[Vision Of Death]], Rank 7: [[True Target]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Reymenda appears as an older woman, just past middle age. Depending on the tale, the Lady of Sacrifice once had children and lost them, or she found that her life was one where having children did not fit her needs and desires. Regardless of the reason, all know that Reymenda now swears an oath to never have children and expects the same of her followers. In exchange for this vow, Reymenda grants her followers the guidance and might they need to bear the responsibility of virtue. While some set out to strike down evil, others rally a community in the wake of a natural disaster, or do something as simple as helping a family by working in their kitchen for an evening when the family is too overburdened by life to cook a meal. No genuinely helpful responsibility is too small for a follower of Reymenda, though they know how to teach others to help themselves or work together, and they also do their best to avoid exploitation when someone grows careless and irresponsible. Reymenda teaches her followers to move on when it appears that others are taking advantage of a follower's generosity.

**Title** Lady of Sacrifice

**Areas of Concern** Childlessness, endings, responsibility

**Edicts** Bring definitive ends to known evils, consider genuine requests for aid, sacrifice when others can't

**Anathema** Adopt or have a child, directly undo the death of another or the ending of something, treat children as a burden or a mistake, withhold news of another's ending

**Religious Symbol** black rose floating in water

**Sacred Animal** mule

**Sacred Colors** black, blue

**Source:** `= this.source` (`= this.source-type`)
