---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Arcane]]", "[[Artifact]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

In preparation for Earthfall, Runelord Zutha bound his soul to the *Gluttonous Tome*—an expansive work that contained the entirety of the runelord's knowledge. To ensure the tome survived the oncoming apocalypse, Zutha divided the book into three parts: the *Kardosian Codex*, the *Black Book*, and the *Bone Grimoire*. Heroes used the *Bone Grimoire* on the risen isle of Xin 7 years ago to finally defeat Zutha, and in doing so, triggered the destruction of the three parts of the *Gluttonous Tome*.

Over the centuries, copies of portions of each book have been made, but these copies lacked any of the original artifacts' powers. One such copy, though, now lies under lock and key in Korvosa's Acadamae: the *Kardosian Fragments*. Originally an incomplete copy of the *Kardosian Codex*, some time after Zutha's defeat, fragments of the destroyed original ended up the property of the Acadamae, and industrious wizardly professors painstakingly restored what they could, pasting these fragments into their incomplete copy of the book. The result is the *Kardosian Fragments*, a potent item that, while only a shadow of the power of the original, remains as dangerous as it is useful.

The *Kardosian Fragments* isn't a spellbook, but it does contain extensive notes on several spells that can be referenced to Learn a Spell. When used in this way, the cost of learning the spell is ignored, as the fragments themselves fulfill this need through remnants of arcane magic that still linger within. The spells that can be learned include [[False Vitality]], [[Invoke Spirits]], [[Summon Undead]], [[Vampiric Exsanguination]], and [[Vampiric Feast]].

If the *Kardosian Fragments* are referenced as part of any attempt to [[Recall Knowledge]] on subjects associated with its contents, it grants a +3 item bonus to the skill check.

**Activate—Embrace the Void** `pf2:1` (manipulate)

**Frequency** once per hour

**Requirements** You are not currently [[Drained]]

**Effect** If your next action this round is to Cast a Spell that has the void trait and you're holding the *Kardosian Fragments*, you gain a number of temporary Hit Points equal to your level × 3. These temporary Hit Points last for 1 hour. When the temporary Hit Points are gone, you become [[Drained]] 1 if you aren't undead.

> [!danger] Effect: The Kardosian Fragments (Temporary Hit Points)

**Destruction** The text in the *Kardosian Fragments* fades away and the book itself becomes a nonmagical tome if an arcane spellcaster of at least 17th level and who follows the envy or lust schools of Thassilonian rune magic spends a year painstakingly refuting, redacting, and revising the contents of this book.

**Source:** `= this.source` (`= this.source-type`)
