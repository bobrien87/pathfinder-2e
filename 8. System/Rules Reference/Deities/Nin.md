---
type: deity
source-type: "Remaster"
domains: "Glyph, Knowledge, Perfection, Undeath"
favored-weapon: "Sword-cane"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Share Lore]], Rank 4: [[Telepathy]], Rank 5: [[Mind Probe]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

No vampire who seeks anything other than more of undeath's secrets dares utter a prayer to Nin, for the vampire deity of unbridled evolution and limitless knowledge seeks to destroy or conquer all who embrace or tolerate weakness. Disciples of Nin believe that undead who waste near immortality on apathy, gluttony, and greed (such as followers of Urgathoa or Zura) remain unworthy of their gifts. Mortals are little more than food that nourishes their empire, and any god who demonstrates compassion toward them is far too complacent to deserve their divine station. True vampires serve Nin through the endless pursuit of knowledge, using methodical analysis to root out flaws and maximize their strengths. Through them, Nin seeks to assemble an army of flawless sentinels that can bring order to Golarion by conquering the weak, including all other deities! Only by doing so will they achieve their ultimate goal: to become the most perfect being in the universe. One supplicates to the Immaculate Solution not on a bent knee, but by poring over dusty tomes to discover the secrets of magic, proving ancient theorems using occult mathematics, or conducting experiments that test the very limits of vampiric might. For vampires who approach the mysteries of the universe as equations to solve, endless power awaits.

**Title** The Immaculate Solution

**Areas of Concern** mathematical laws of undeath, unsolved mysteries, vampires

**Edicts** become a paragon of vampiric perfection, eliminate vampiric weaknesses using analysis and experimentation, punish those who restrict the free exchange of information

**Anathema** demonstrate apathy or complacency toward self-improvement, fail to cooperate or share information with another worshipper of Nin, refuse to attempt to find a solution when presented with a problem

**Religious Symbol** two skulls facing atop a grimoire in a pool of blood

**Sacred Animal** spider

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
