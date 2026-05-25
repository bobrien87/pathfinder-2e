---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Divine]]", "[[Holy]]", "[[Intelligent]]", "[[Laminar]]"]
price: "{'value': {}}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +23; precise vision (darkvision) 60 feet, imprecise hearing 30 feet

**Communication** telepathy (Celestial, Common)

**Skills** Diplomacy +25, Religion +25

**Int** +4, **Wis** +4, **Cha** +6

**Will** +25

A suit of [[Autumn's Embrace]] armor can gain sapience when lovingly crafted by a fey monarch of sufficient power; a suit of faerie queen's bower is one such example. The armor is happy to give you and your companions counsel, hoping to guide you on a path of benevolence and aid you in battles against forces that seek to cause harm to the natural world. It refuses access to its magic to anyone who causes undue harm to plants or animals.

In addition to the features and activation of autumn's embrace, faerie queen's bower has the following activation.

**Activate** `pf2:2` (aura, concentrate)

**Frequency** once per day

**Effect** You call forth a storm of leaves from *autumn's embrace*. These leaves swirl in a @Template[emanation|distance:20] for 1 minute. Creatures within the area are [[Concealed]], and creatures outside the area are concealed to creatures within the leaves. However, you can see through this concealment. You can Dismiss the activation.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The armor casts 4th-rank [[Safe Passage]], with the protected area beginning from your square and extending to a place of relative safety.

**Source:** `= this.source` (`= this.source-type`)
