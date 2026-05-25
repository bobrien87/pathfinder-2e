---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Fate, Time"
favored-weapon: "Whip"
divine-font: "Harm, Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Ant Haul]], Rank 3: [[Insect Form]], Rank 9: [[Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

No one knows where and when Aakriti came into existence. Some divine scholars surmise they've always been a part of the primordial soup of creation. The most popular theory, as reflected in various religious iconography, is that Aakriti is the pupae of a primordial deity that took damage in their chrysalis state and became unable to molt into their final form.

Known as Aakriti the Evershifting, this ooze deity represents the ever-evolving nature of creation and life as well the potential of the unknown. New life crawls forth from their primordial depths in an explosion of the bizarre and colorful, adjusting in their own individual ways to the challenges of existence. As each life moves through the various cycles of growth over time, they must be flexible and adapt to the changes, especially at its crux—the state of transition. Sometimes a new step involves a frightening destruction of identity, but it should be embraced instead of feared, as the primordial nothingness holds the potential for new creations beyond the wildest imaginings of one's current self. Those who stay rigid in their beliefs or refuse to change will become trapped in the shells of their old selves and crush themselves in their struggle to avoid growth. Aakriti also has no love for those who entrap creatures into a form unwillingly and will sometimes intercede against them.

**Title** The Evershifting

**Areas of Concern** Discovery, life, ooze, potential

**Edicts** Create without reservation, help others unlock their true potential, observe the mysteries of life

**Anathema** Fail to study a new creature if safely able, force a creature to live in the wrong body, reject creatures or information due to bigoted or rigid beliefs

**Religious Symbol** molting cicada

**Sacred Animal** insect

**Sacred Colors** all

**Source:** `= this.source` (`= this.source-type`)
