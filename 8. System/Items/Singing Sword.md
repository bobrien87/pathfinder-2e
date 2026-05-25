---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Intelligent]]", "[[Occult]]", "[[Versatile p]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +11; precise vision 30 feet, imprecise hearing 30 feet

**Communication** speech (Common and four other common languages)

**Skills** Performance +15

**Int** +2, **Wis** +2, **Cha** +4

**Will** +13 (+17 against attempts to quiet its singing)

A *singing sword* is a *+1 striking* longsword imbued with the consciousness of a boisterous bard, and therefore constantly sings at all times. A *singing sword* can't stop singing and in fact communicates in no way other than by singing. A successful Diplomacy or Intimidation check against its Will DC can convince it to quiet its singing to a whisper for 10 minutes, or 20 minutes on a critical success, though it quickly grows displeased at anyone who attempts this repeatedly. The *singing sword* can spend its actions to attack on its own, with the effects of a *dancing* weapon's activation, except that its attack modifier is +12. Additionally, it can perform the following activations; each casts a composition spell and follows all the usual rules for compositions.

**Activate—Courageous Anthem** A (concentrate)

**Frequency** once per minute

**Effect** The *singing sword* casts [[Courageous Anthem]].

**Activate—Rallying Anthem** A (concentrate)

**Frequency** once per minute

**Effect** The *singing sword* casts [[Rallying Anthem]].

**Activate—Counter Performance** R (concentrate)

**Frequency** once per hour

**Trigger** You or an ally within 60 feet rolls a saving throw against an auditory effect

**Effect** The *singing sword* casts [[Counter Performance]].

**Source:** `= this.source` (`= this.source-type`)
