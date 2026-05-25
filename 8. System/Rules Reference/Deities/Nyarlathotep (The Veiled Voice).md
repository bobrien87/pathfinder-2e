---
type: deity
source-type: "Remaster"
domains: "Ambition, Fate, Knowledge, Magic"
favored-weapon: "Bo-staff"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Message Rune]], Rank 2: [[Blur]], Rank 3: [[Hypercognition]], Rank 4: [[Vapor Form]], Rank 5: [[Subconscious Suggestion]], Rank 6: [[Never Mind]], Rank 7: [[Contingency]], Rank 8: [[Disappearance]], Rank 9: [[Phantasmagoria]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Nyarlathotep is a being of a thousand shapes, each of which has a name, such as the Haunter of the Dark or the Veiled Voice. Because he has walked the world in mortal form, Nyarlathotep is unique among the Outer Gods for appearing comprehensible and understandable—but this is a facade. The Crawling Chaos, as he is also known, appears humanlike not because he identifies with mortal concerns or cares for his mortal followers, but because a mortal shape makes it easier for him to do his work: spreading the influence of the Outer Gods.

**Title** The Veiled Voice

**Areas of Concern** Dangerous secrets, long-term plans, reckless innovation

**Edicts** Innovate destructive alchemy or magic, instigate conflict between your enemies, share dangerous secrets

**Anathema** None

**Religious Symbol** a pair of runed lips pursed in a whisper

**Sacred Animal** panther

**Sacred Colors** black, purple

**Source:** `= this.source` (`= this.source-type`)
