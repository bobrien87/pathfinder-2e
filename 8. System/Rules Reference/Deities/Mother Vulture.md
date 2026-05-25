---
type: deity
source-type: "Remaster"
domains: "Change, Death, Decay, Nature"
favored-weapon: "Sickle"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Aerial Form]], Rank 6: [[Cursed Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Though she usually appears as a blind young woman, in her natural form, the Flesheater is an enormous, bloated creature with four wings and two long necks topped with masked heads and gaping maws. Mother Vulture reflects the dualistic process of decay. She is a vicious killer whose feasts stain the ground, representing the death inherent in decay, but also a thoughtful mother, representing the new life that can take root in the fertile soil left in the wake of destruction. She is reviled by many, for she is the ugliness of reality on full display, but there are some who can see the beauty hidden within her stark pragmatism. Mother Vulture's mortal worshippers, who often dwell in deserts and swamps, revere her as the patron of consumption, renewal, and transformation. In this last aspect, she judges those souls who sought redemption in life, deciding whether their atonement was sufficient to avoid an undesired afterlife.

**Title** The Flesheater

**Areas of Concern** Consumption, renewal, transformation

**Edicts** Recycle rot and waste into useful creations, eat the flesh of your own people, kill without mercy if it benefits your community, help to raise children

**Anathema** Poison insects or scavengers, waste food or good materials, allow rot to poison an area, create undead

**Religious Symbol** two crossed diagonal lines with an empty circle above and a filled circle below

**Sacred Animal** vulture

**Sacred Colors** gray, yellow

**Source:** `= this.source` (`= this.source-type`)
