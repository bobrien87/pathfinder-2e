---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Grimoire]]", "[[Intelligent]]", "[[Magical]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +17; precise vision 30 feet, imprecise hearing 30 feet, imprecise sense of heat 30 feet

**Communication** telepathy (Common, Pyric, and two other common languages)

**Skills** Arcana +21, Fire Lore +23, Nature +17

**Int** +4, **Wis** +0, **Cha** +5

**Will** +17

A *kindled tome* is a [[Book of Lingering Blaze]] awakened to sapience and imbued with an enthusiasm for fire. It encourages you to learn new fire spells to inscribe within its pages. When you attempt a skill check to [[Learn a Spell]] to add a spell with the fire trait to the *kindled tome*, you treat your result as one step better than you rolled. The tome can be disparaging about other spells as "a waste of good page space," especially if those spells have the cold or water traits. In addition to the activation of a *book of lingering blazes*, a *kindled tome* has the following activations.

**Activate** `pf2:1` envision (spellshape)

**Frequency** once per day

**Effect** If your next action is to Cast a Spell dealing fire damage that you prepared from this grimoire, you superheat the flames, allowing the spell to ignore up to 10 resistance to fire of creatures affected by the spell.

**Activate** R (concentrate)

**Frequency** once per hour

**Trigger** You Cast a Spell with the fire trait

**Effect** The tome makes the flames linger, dealing 2d6 persistent,fire damage to all you hit with or who fail the saving throw against the effect (doubling on a critical success on a spell attack and on a critical failure on a saving throw).

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The tome casts [[Fireball]] at 5th rank to your specifications.

**Source:** `= this.source` (`= this.source-type`)
