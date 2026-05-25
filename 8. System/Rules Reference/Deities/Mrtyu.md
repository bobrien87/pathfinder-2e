---
type: deity
source-type: "Remaster"
domains: "Death, Passion, Repose, Sorrow"
favored-weapon: "Greatsword"
divine-font: "Harm, Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Weapon Storm]], Rank 5: [[Wave Of Despair]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Everyone who dies has a final thought, a last word, an emotion swollen in the heart, or a feeling caught in the throat. For Mrtyu, a mortal soldier, those last words were a reflection on one thing: love. This was a final thought that intrigued the Lady of Graves, for she had never seen its like before. She wooed the fallen soldier in the afterlife, and in growing to understand him, she understood the passions of all who live.

Mrtyu became Death's Consort, the psychopomp usher of poetry, trauma, and war. He cares for the souls of soldiers, murder victims, those who die gripped by their strongest emotions, and those who take their own lives. When a soul is too tormented for rest, Mrtyu feels their pain in his own heart when they rise from their graves. His realm, the Garden Anima, is a peaceful refuge within Pharasma's Court where those who suffer traumatic deaths can contemplate and work to understand their fates in safety.

**Title** Death's Consort

**Areas of Concern** Poetry, trauma, war

**Edicts** Destroy undead, honor fallen soldiers, hear the confessions of the dying, put malcontent spirits to rest

**Anathema** Create undead, deny your emotions, shame others for emotional outbursts

**Religious Symbol** circle with five curved lines extending from it

**Sacred Animal** crane

**Sacred Colors** gray and pink

**Source:** `= this.source` (`= this.source-type`)
