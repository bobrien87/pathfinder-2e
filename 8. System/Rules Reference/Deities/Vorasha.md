---
type: deity
source-type: "Remaster"
domains: "Decay, Magic, Water, Wyrmkin"
favored-weapon: "Spiked-chain"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Spider Sting]], Rank 5: [[Toxic Cloud]], Rank 8: [[Monstrosity Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Vorasha is considered the most powerful of the daemonic harbingers, likely because of her close ties to Trelmarixian, the Rider of Famine. Some say that he has had a subtle influence on the Ophidian's rise through the ranks. However, Vorasha has plans of her own to become a Rider in her own right, focusing on poisons and incurable toxins. She schemes from the Writhing Palace, a vast garden of poisonous plants infested with venomous serpents. Because this domain lies wholly within the Withered Court, Trelmarixian's realm, Vorasha suspects the Rider of Famine is aware of her every move.

Vorasha appears as a scaled draconic humanoid with clawed hands and feet. She has a tangle of scarlet-and-emerald snakes as hair that are constantly writhing. As the Lady of Toxicity, she wears a flowing green gown that drips with poisons.

**Title** The Ophidian

**Areas of Concern** Incurable afflictions, poisons, toxicity

**Edicts** Lay your enemies low through deceit and subtlety, preserve your patience for longterm goals, venerate all scaled creatures

**Anathema** Cultivate or maintain a garden of nonpoisonous plants, intentionally harm a venomous serpent not in self-defense

**Religious Symbol** oruroboros and jackal head

**Sacred Animal** viper

**Sacred Colors** green, yellow

**Source:** `= this.source` (`= this.source-type`)
