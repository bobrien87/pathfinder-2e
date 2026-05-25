---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 250}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tattoo resembles an animal's fangs, claws, or similar natural weapons, letting you wield such weapons and turn into the same beast. When you receive the tattoo, choose the animal from among the following: ape, bear, bull, canine, cat, deer, frog, shark, or snake. You can ask questions of, receive answers from, and use the Diplomacy skill with animals of that kind. This tattoo is usually located on the body part or parts it's meant to transform—on the back of the hands for claws, around the mouth for jaws, on the forehead for horns, and so on.

**Activate** `pf2:1` (concentrate, morph)

**Effect** You gain an unarmed attack matching the tattoo for 1 minute. It has the same damage as your best unarmed attack and has the same traits. Its damage type is bludgeoning for a fist or frog's jaws; piercing for an antler, fangs, horns, or most jaws; or slashing for claws.

**Activate** `pf2:2` (concentrate, polymorph)

**Effect** The tattoo casts 3rd-rank [[Animal Form]] to transform you into the animal that matches your tattoo.

**Source:** `= this.source` (`= this.source-type`)
