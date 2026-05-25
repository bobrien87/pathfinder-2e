---
type: deity
source-type: "Remaster"
domains: "Destruction, Vigil, Water, Wyrmkin"
favored-weapon: "Whip"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 2: [[Brine Dragon Bile]], Rank 3: [[Feet To Fins]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As boastful as he is bestial, Ragadahn the Water Lord is the Eldest of oceans, linnorms, and sinuous spirals. He appears as a great serpentine dragon in the First World's seas, but he is widely traveled and takes other forms as needed to pursue both martial conquests and amorous affairs. He is widely believed to be the progenitor of all linnorms, and he claims to be the progenitor of all dragons. True dragons stridently contest this assertion, although they wisely decline to do so when in Ragadahn's majestic presence. Failure to deliver proper respect to the arrogant Ragadahn invites his legendary ire, and no supplicant can ever be too flattering for his tastes. Yet for all his tempestuous nature, he is wise, and he holds much otherwise lost and forgotten knowledge.

**Title** The Water Lord

**Areas of Concern** Linnorms, oceans, spirals

**Edicts** Draw spirals, seek primordial secrets, use poison, always carry water

**Anathema** Suffer a linnorm's death curse, destroy a fossil

**Religious Symbol** blue ouroboros

**Sacred Animal** sea snake

**Sacred Colors** blue

**Source:** `= this.source` (`= this.source-type`)
