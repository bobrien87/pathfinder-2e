---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Two-Headed Troll"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Troll"
trait_04: "Wood"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Jotun"
skills:
  - name: Skills
    desc: "Athletics +18, Intimidation +17"
abilityMods: ["+6", "+1", "+6", "-2", "+4", "+3"]
abilities_top:
  - name: "Easily Misled"
    desc: "The two-headed troll takes a –4 circumstance penalty to their Perception DC against Deception checks."
  - name: "Independent Brains"
    desc: "Each of a two-headed troll's heads rolls their own initiative and has their own turn. Neither head can Delay. At the start of a head's turn, that head gets 2 actions and 1 reaction. Each brain controls one arm, but both can move the legs. Any ability or item that would sever a two-headed troll's head (such as a vorpal weapon) doesn't cause the two-headed troll to die if they still have their other head, but does cause them to lose the turns, actions, and reactions of the severed head. Mental effects that target a single creature affect only one of the troll's heads."
armorclass:
  - name: AC
    desc: "24; **Fort** +19, **Ref** +15, **Will** +14"
health:
  - name: HP
    desc: "190; **Weaknesses** electricity 10, fire 10"
abilities_mid:
  - name: "Regeneration 20 (Deactivated by Electricity or Fire)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Head Regrowth"
    desc: "A two-headed troll's regeneration can regrow a severed head. After regaining Hit Points from regeneration, the two-headed troll attempts a DC 10 flat check. On a success, a missing head is fully restored. If a two-headed troll loses their last remaining head, they die immediately."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +18 (`pf2:1`) (reach 10 ft.), **Damage** 2d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Club +13 (`pf2:1`) (thrown 10), **Damage** 2d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (reach 10 ft.), **Damage** 2d12+8 piercing"
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, reach 10 ft.), **Damage** 2d8+8 slashing"
spellcasting: []
abilities_bot:
  - name: "Collaborative Chomp"
    desc: "`pf2:2` The troll makes a claw Strike and Grabs a single target. If both are successful, the other head can use their reaction to make a jaws Strike against that creature."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

After a particularly severe head injury, a troll might regrow two heads, with each taking on fragments of the old personality and its responsibilities over the body. As separated parts of a whole, the heads find it difficult to agree on any but the most basic tasks. These tasks usually involve gathering food to satisfy two mouths, even if they share a single cavernous stomach. Dread tales of two-headed trolls' ravenous appetites are whispered of in homesteads throughout the lands of the Inner Sea. It's a custom for parents to invoke the two-headed troll as a warning to misbehaving children. "Finish your chores," a parent might say to a stubborn child, "or a two-headed troll will snatch you away at night and swallow you whole!" It's unclear why such a morbid tradition gained traction, but it's an undeniable fact that two-headed trolls have an appetite for "nibbles"—creatures small enough to devour with one bite.

Towering brutes with slavering jaws and razor-sharp claws, trolls are voracious predators. A connection to the land not only rebuilds their bodies but creates countless varieties of trolls, each a reflection of the terrain that they draw upon. Trolls who migrate into new areas slowly transform as each body part is regenerated, leading to aberrant growth as new flesh tangles with the old.

```statblock
creature: "Two-Headed Troll"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
