---
type: deity
source-type: "Remaster"
domains: "Dreams, Earth, Family, Might"
favored-weapon: "War-flail"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Mindlink]], Rank 4: [[Mountain Resilience]], Rank 7: [[Duplicate Foe]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Known as the Twins, Imbrex is the mysterious Eldest of twins, statues, and endings. Appearing as two immense stone statues hundreds of feet tall holding hands and looking outward, Imbrex neither moves nor speaks. The Eldest sometimes communicates with telepathic utterances that rend minds or deliver psychic enlightenment, but they more often express their will through startlingly realistic dreams that sometimes manifest into strange life. An entire city named Anophaeus sprawls at Imbrex's four feet, populated by jaded urbanites, eager aspirants, and prowling dreamcreatures made real. An unusually high proportion of those born in Anophaeus are twins, and twins are also common among Imbrex's worshippers. Although Imbrex appears timeless in form, they are intrigued by dramatic endings, particularly apocalypses, and have foreknowledge of disasters to come.

**Title** The Twins

**Areas of Concern** Endings, statues, twins

**Edicts** Pursue your own goals, bring things to their proper ending, split things in half or otherwise create pairs

**Anathema** Offend Imbrex

**Religious Symbol** clasped hands

**Sacred Animal** hibernating animals

**Sacred Colors** gray, silver

**Source:** `= this.source` (`= this.source-type`)
