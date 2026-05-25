---
type: deity
source-type: "Remaster"
domains: "Family, Might, Nightmares, Trickery"
favored-weapon: "Falchion"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Spider Sting]], Rank 2: [[Animal Form]], Rank 4: [[Nightmare]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Lamashtu is the goddess of nightmares and aberrance. She was the first demon lord to achieve true godhood. After murdering Curchanus, a now mostly forgotten god of beasts, travel, and endurance, she wrested his dominion over beasts from his dying body to gain divinity. Now, she's revered as the Mother of Monsters and the Queen of Demons. Legends say that nearly all Golarion's foul creatures sprang from her polluted womb. Loathsome monsters account for most of her worshippers, though she also resonates with individuals who consider themselves outcasts from the world or seek to transform all mortalkind into ravenous beasts.

**Title** Mother of Monsters

**Areas of Concern** aberrance, monsters, nightmares

**Edicts** bring power to outcasts and the downtrodden, indoctrinate others in Lamashtu's teachings, make the beautiful monstrous, reveal the corruption and flaws in all things

**Anathema** attempt to change that which makes you different, provide succor to Lamashtu's enemies

**Religious Symbol** three-eyed jackal

**Sacred Animal** jackal

**Sacred Colors** red, yellow

**Source:** `= this.source` (`= this.source-type`)
