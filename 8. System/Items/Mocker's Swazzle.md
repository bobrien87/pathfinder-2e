---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A swazzle is a device made of two strips of metal bound with sinew and around a reed that, when held to the mouth, causes the user's voice to take on a distinctive rasping tone. Swazzles are often used by street puppeteers to give their puppets' voices a unique and memorable timber. A mocker's swazzle, though, has a different use—rather than simply giving voices to troublemaking puppets, it helps a performer fight back against hecklers in a crowd.

**Activate—Heckle the Heckler** `pf2:r` (auditory, emotion, linguistic, manipulate, mental)

**Frequency** once per hour

**Trigger** A creature within 30 feet of you attempts and fails to [[Demoralize]] you

**Effect** You quickly fire a retort back at the triggering creature, mocking its failed attempt in a way that makes it laugh at its own ineptitude; you cast [[Laughing Fit]] (DC 30 [[Will]] save) on the triggering creature.

**Activate—Mocking Spell** `pf2:1` (auditory, linguistic, spellshape)

**Frequency** once per day

**Effect** You direct a quick bit of insulting mockery at a creature who can understand you that's within earshot. If your next action is to cast a mental spell that targets only that creature, that creature takes a –1 item penalty to any saving throw against the spell and, regardless of the result of the saving throw, becomes [[Off Guard]] until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
