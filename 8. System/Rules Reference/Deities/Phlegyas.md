---
type: deity
source-type: "Remaster"
domains: "Creation, Duty, Knowledge, Repose"
favored-weapon: "Longbow"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Illusory Object]], Rank 3: [[Threefold Aspect]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Before she was a psychopomp usher, Phlegyas was mortal. The most brilliant artist of her age, she was also vain and prideful, and when her arrogance led to blasphemy she was cast out from Shelyn's church. In her excommunication, the clergy sought to strike her name from history, but they failed. Phlegyas's legacy did more than merely survive; the artist's name and achievements went on to last forever.

When Phlegyas came before Pharasma for judgment, the Lady of Graves saw a mortal who would defy death, the gods, or even the multiverse itself should it dare stand in her way; who challenged and redefined her gender in life and then her fate in death; who would not compromise on showing the world the truest version of herself, forever. Pharasma saw in Phlegyas a yearning to be known fundamentally to all mortals, and so elevated her into an usher of her court.

**Title** The Consoler of Atheists

**Areas of Concern** Atheists, legacies, reincarnation

**Edicts** Allow atheists to hold their beliefs, challenge what is presupposed, forge a lasting legacy, live authentically, take pride in your work

**Anathema** Allow your accomplishments to go unattributed, destroy another artist's legacy, misattribute or obscure the authorship of a work of art

**Religious Symbol** two circles overlapping vertically

**Sacred Animal** coral

**Sacred Colors** red

**Source:** `= this.source` (`= this.source-type`)
