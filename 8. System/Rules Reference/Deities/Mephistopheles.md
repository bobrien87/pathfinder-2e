---
type: deity
source-type: "Remaster"
domains: "Glyph, Knowledge, Secrecy, Tyranny"
favored-weapon: "Trident"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Message Rune]], Rank 2: [[Blistering Invective]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The archdevil Mephistopheles was shaped of the ashes and fire of Hell itself to convey the plane's will. The lord of Caina, Hell's eighth layer, he is a conniving schemer and a brilliant politician, quick to offer insults both blatant and cloaked behind silvered words. A master of rule, law, and words, he is the creator of the renowned agreements known as infernal contracts, crafted to damn mortal souls through their own ambitions. He views mortals as nothing more than a source of power for the infernal realm, but he nevertheless has followers who share his affinity for the power of law and loophole.

**Title** The Crimson Son

**Areas of Concern** Contracts, devils, secrets

**Edicts** Master laws and use them to your benefit, enable the desperate, excoriate others with veiled mockery

**Anathema** Break a contract you made, get caught breaking the law

**Religious Symbol** trident and ring

**Sacred Animal** mockingbird

**Sacred Colors** red, yellow

**Source:** `= this.source` (`= this.source-type`)
