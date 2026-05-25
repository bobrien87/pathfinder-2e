---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Intelligent]]", "[[Invested]]", "[[Primal]]"]
price: "{'value': {}}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +30; precise vision (darkvision) 30 feet, imprecise hearing 30 feet

**Communication** telepathy (Common and two other common languages; speak with plants)

**Skills** Diplomacy +28, Medicine +32, Nature +32

**Int** +6, **Wis** +10, **Cha** +5

**Will** +32

An encounter with a toshigami, the enigmatic kami who protect cherry trees, is rare, though often sought after and treasured by those who achieve such an encounter. Only a handful of mortals can truthfully claim to have seen a toshigami, let alone met one, though many popular fireside tales tell of virtuous souls receiving a toshigami's blessing to fight for a worthy cause. Such stories have a basis in fact; every so often, a toshigami gives a worthy mortal a flower from their ward, time-locked in perfect bloom and granted sapience. Such *toshigami blossoms* are more sociable than their creators. Like toshigami, a blossom has a strong curiosity about the mortal world. If you wear a *toshigami blossom*, it can intercede for you, helping you make a good impression.

A *toshigami blossom* has the following activations.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The blossom casts [[Nature's Pathway]] on you to your specifications. If you target only cherry trees, the spell is cast at 6th rank.

**Activate** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** The blossom casts [[Soothing Blossoms]] to your specifications.

**Activate** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** The blossom sends a flurry of cherry blossoms outward in a @Template[burst|distance:20] that lasts 1 round. You and your allies can see through these blossoms. To all other creatures, creatures within the cloud of blossoms become [[Concealed]], and creatures outside the cloud become concealed to creatures within it. When you or an ally succeeds with a Strike against a creature in the blossoms, the Strike deals an additional 1d6 mental and an additional 1d6 void to living creatures, or an additional 1d6 vitality to undead.

**Source:** `= this.source` (`= this.source-type`)
