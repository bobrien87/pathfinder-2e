---
type: deity
source-type: "Remaster"
domains: "Change, Decay, Nature, Plague"
favored-weapon: "Scimitar"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 2: [[Fungal Hyphae]], Rank 5: [[Plant Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Cyth-V'sug, Prince of the Blasted Heath, is the demon lord of disease, fungus, and parasites. Originally a qlippoth lord, he was exiled by his peers for accepting mortal worshippers. Transformed into one of the demons he despises, Cyth-V'sug seeks to devour all life to put an end to demons and, ultimately, himself. He most often appears as an enormous draconic figure of snarled vines, fungal growths, and flailing tentacles. Cyth-V'sug is most often worshipped by recluses who seek to bring decay and destruction to their environs, though denizens of the Darklands also pay homage to him.

**Title** Prince of the Blasted Heath

**Areas of Concern** Disease, fungus, parasites

**Edicts** Corrupt all that exists with parasites or fungus, promote the growth of fungus, feast on rotten flesh or fungus

**Anathema** Purify your food, cure a disease or kill a parasite, tolerate another demon lord or their servants (except Treerazer)

**Religious Symbol** moldy spiraling tentacle

**Sacred Animal** centipede

**Sacred Colors** green, yellow

**Source:** `= this.source` (`= this.source-type`)
