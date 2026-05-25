---
type: deity
source-type: "Remaster"
domains: "Family, Healing, Nature, Pain"
favored-weapon: "Ranseur"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 2: [[Animal Form]], Rank 6: [[Petrify]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Stag Mother of the Forest of Stones is quite possibly the oldest surviving spirit guide left in existence, certainly the oldest still actively worshipped in Sarkoris today. Long ago, she was the premier spirit worshipped in the region of Sarkoris known as the Stonewilds, and the druids of the Circle of Hierophants (or their distant predecessors) erected stone menhirs as monuments depicting the Stag Mother and her fellow spirit guides guiding and protecting the people of the region. When the Worldwound opened and demons poured forth, the Stag Mother gathered many Sarkorians to safety in her demesne, a region of the Stonewilds known as the Forest of Stones. Between the Stag Mother's godly power and the might of the lesser spirit guides that gathered under her banner, the Forest of Stones may have stood as a bastion of nature capable of withstanding even the unprecedented demonic incursion, but sadly a group of druids in the region lost faith in their long-time protectors. When the horrific perversions of druidic faith known as the Stonewild Sect transformed themselves into undead, their twisted power spread through the bonds some shared with the spirit guides, killing many of the weaker guides instantly and transforming others into dark mockeries of their former selves. In despair, the Stag Mother retreated far from the front lines of the battle, sheltering a precious few. While her worship has once again begun to spread beyond her forest home, the Stag Mother's trust of her human worshippers has been deeply undermined, and she demands that the spirit guides who live within her dominion do not form bonds with mortals or accept new god callers without her express permission.

**Title** She Who Listens

**Areas of Concern** Druids, motherhood, sacred nature

**Edicts** Act as a responsible steward of your environment, provide shelter and succor for women and children in need

**Anathema** Harm a pregnant mother or innocent child, including animals

**Religious Symbol** rack of antlers made of stone

**Sacred Animal** stag

**Sacred Colors** red, brown, white

**Source:** `= this.source` (`= this.source-type`)
