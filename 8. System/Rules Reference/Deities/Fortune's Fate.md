---
type: deity
source-type: "Remaster"
domains: "Ambition, Dreams, Fate, Luck"
favored-weapon: "Fighting-fan"
divine-font: "Heal"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Invisibility]], Rank 7: [[True Target]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Luck is more than just a flick of a card or a roll of the dice; what some consider pure chance can often be attributed to an individual's drive to achieve a goal. The gods of luck who make up Fortune's Fate understand and promote this little "secret" of the cosmos. They don't believe in simply letting circumstance guide everything, which could lead to destructive chaos. Followers of Fortune's Fate tend to enter situations understanding the odds and know that a gold coin placed in the right hand or a well-timed spell can tip those odds in their favor. They also know that every plan contains some element of risk and they thrive by blurring the line between luck and daring.

**Pantheon Members** Bes, Chaldira Zuzaristan, Desna, Kofusachi, The Lantern King, Nivi Rhombodazzle

**Areas of Concern** con artists, productive mischief, strategic gamblers, tilting the scales of luck

**Edicts** defeat challenges through the use of dashing plans that have some element of risk involved, encourage others to take chances, use the element of surprise whenever possible

**Anathema** attribute happy accidents or purely lucky outcomes to be the result of your skill alone, cheat or use unfair tactics after you've committed yourself to following specific rules (cheating other times is fine), place your fate in chance without applying any effort

**Religious Symbol** golden-furred rabbit's foot

**Source:** `= this.source` (`= this.source-type`)
