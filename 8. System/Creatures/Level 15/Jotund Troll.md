---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jotund Troll"
level: "15"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Mutant"
trait_04: "Troll"
trait_05: "Wood"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]]"
languages: "Jotun"
skills:
  - name: Skills
    desc: "Athletics +29, Intimidation +27"
abilityMods: ["+8", "+4", "+8", "-1", "+6", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "35; **Fort** +31, **Ref** +24, **Will** +23"
health:
  - name: HP
    desc: "360; **Weaknesses** electricity 15, fire 15"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Regeneration 40 (Deactivated by Electricity or Fire)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Furious Roar"
    desc: "`pf2:r` **Trigger** The jotund troll takes electricity or fire damage <br>  <br> **Effect** The jotund troll uses their Cacophonous Roar and, if they're aware of the damage's source, can Stride toward it. If the jotund troll has persistent fire damage, they attempt a DC 15 flat check to remove it."
  - name: "Head Regrowth"
    desc: "A jotund troll's regeneration can regrow severed heads. After regaining Hit Points from regeneration, the jotund troll attempts a DC 8 flat check. On a success, one missing head is fully restored; on a critical success, two missing heads are fully restored. If a jotund troll loses their last remaining head, they die immediately."
  - name: "Reactive Heads"
    desc: "A jotund troll gains an extra reaction per round for each of their heads beyond the first, which they can use only to make Reactive Strikes with their jaws or to Fast Swallow. They can't use more than 1 reaction for the same triggering action, even if a creature leaves several squares within their reach, and must use a different head for each Reactive Strike. Whenever one of the jotund troll's heads is severed, the troll loses 1 of their extra reactions per round."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Fast Swallow"
    desc: "`pf2:r` **Trigger** The jotund troll Grabs a creature with their jaws <br>  <br> **Effect** The troll uses Swallow Whole."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +29 (`pf2:1`) (reach 15 ft.), **Damage** 3d12+14 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +29 (`pf2:1`) (agile, reach 15 ft.), **Damage** 3d10+14 slashing"
spellcasting: []
abilities_bot:
  - name: "Cacophonous Roar"
    desc: "`pf2:1` The jotund troll roars from all their heads, mystically distorting the listener's mind. Each non-troll creature in a @Template[type:emanation|distance:100] must attempt a DC 34 [[Will]] save. <br> - **Critical Success** The creature is unaffected and is temporarily immune for 24 hours. <br> - **Success** The creature is [[Stupefied 1]] for 1 round. <br> - **Failure** The creature is [[Stupefied 2]] for 1 round. <br> - **Critical Failure** The creature is [[Confused]] for 1 round."
  - name: "Ravenous Jaws"
    desc: "`pf2:2` The jotund troll makes a number of jaws Strikes up to their number of heads, each against a different target. These attacks count toward the troll's multiple attack penalty, but the penalty doesn't increase until after the jotund troll makes all of these attacks."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Swallow Whole"
    desc: "`pf2:1` Medium, @Damage[(3d12+8)[bludgeoning]], Rupture 36 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Jotund trolls are gigantic, nine-headed horrors who prowl frigid moors, marshes, and wastelands, often alone and always ravenous. While each of the jotund troll's nine heads possess their own brains and senses, they bicker with each other much less than the heads of a two-headed troll. Yet the heads still argue, particularly over which of them gets to eat. The fact that all nine maws lead to the same shared stomach makes little difference in such culinary disagreements. Many scholars echo a story that jotund trolls resemble the first trolls, titans cast out of Elysium and cursed for their crimes against the gods. The jotund trolls themselves make no claims to such a heritage, however, and those concerned with such matters claim the father of all trolls arose in the Outer Rifts. Individual jotund trolls either begin their life as a common troll or, far more rarely, are born to a jotund troll parent. To the jotund trolls, their nine heads are a crown of rule that marks them as above the natural order and free from its laws.

Towering brutes with slavering jaws and razor-sharp claws, trolls are voracious predators. A connection to the land not only rebuilds their bodies but creates countless varieties of trolls, each a reflection of the terrain that they draw upon. Trolls who migrate into new areas slowly transform as each body part is regenerated, leading to aberrant growth as new flesh tangles with the old.

```statblock
creature: "Jotund Troll"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
