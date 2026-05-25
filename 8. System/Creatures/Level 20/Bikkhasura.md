---
type: creature
group: ["Asura", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bikkhasura"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+36; [[Darkvision]], [[Scent]] (imprecise) 60 feet, [[Truesight]] (precise) 60 feet"
languages: "Common, Diabolic (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +33, Athletics +38, Diplomacy +36, Intimidation +34, Performance +34, Religion +35, Stealth +33"
abilityMods: ["+10", "+7", "+10", "+7", "+7", "+8"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Curse of Wisdom"
    desc: "**Saving Throw** DC 42 [[Will]] save <br>  <br> **Stage 1** 12d6 mental damage and target cannot use reactions (1 round) <br>  <br> **Stage 2** 14d6 mental damage and the target is [[Slowed]] 2 (1 round) <br>  <br> **Stage 3** 15d6 mental damage and target is [[Paralyzed]] (1 round)"
armorclass:
  - name: AC
    desc: "44; **Fort** +35, **Ref** +32, **Will** +32"
health:
  - name: HP
    desc: "380; **Immunities** curse, disease, illusion, poison, polymorph"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+2 Status to All Saves vs. Mental"
    desc: ""
  - name: "Regeneration 20"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Inescapable Aura"
    desc: "30 feet. Creatures cannot teleport into or out of the bikkhasura's aura. Creatures attempting to teleport into the aura instead teleport to the nearest edge of the aura. Any attempts to teleport out of the aura are automatically disrupted."
  - name: "Reactive Strike"
    desc: "`pf2:r` The bikkhasura gains 5 additional reactions at the beginning of each of their turns that they can use only for a Reactive Strike. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Horrific Glimpse"
    desc: "`pf2:0` **Frequency** once per round <br>  <br> **Trigger** The bikkhasura uses Glorious Visage <br>  <br> **Effect** The bikkhasura explodes with spiritual energy, dealing @Damage[9d6[spirit]|options:area-damage] damage to all creatures within 30 feet. This ability has the holy trait if the bikkhasura has the holy trait and the unholy trait when the bikkhasura has the unholy trait."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spirit Blade +37 (`pf2:1`) (magical, reach 15 ft., versatile p), **Damage** 4d6+15 slashing plus 4d6 spirit"
  - name: "Melee strike"
    desc: "Jaws +37 (`pf2:1`) (magical), **Damage** 4d6 poison plus 4d10+15 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Claw +35 (`pf2:1`) (agile, magical), **Damage** 4d8+15 slashing plus 1d6 spirit plus [[Curse Of Wisdom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44, attack +0<br>**10th** [[Freeze Time]]<br>**9th** [[Implosion]], [[Metamorphosis]], [[Wails of the Damned]]<br>**6th** [[Cursed Metamorphosis]], [[Truesight]] (Constant)<br>**5th** [[Wave of Despair]] (At Will)<br>**4th** [[Planar Tether]], [[Translocate]] (At Will), [[Unfettered Movement]], [[Weapon Storm]]<br>**2nd** [[Dispel Magic]]<br>**1st** [[Harm]], [[Heal]]"
abilities_bot:
  - name: "Bladestorm"
    desc: "`pf2:2` **Requirements** The bikkhasura is holding six spirit blades <br>  <br> **Effect** The bikkhasura makes up to six spirit blade Strikes, each against a diferent target. These attacks count toward the bikkhasura's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks."
  - name: "Direct Spirit Blades"
    desc: "`pf2:2` **Requirements** The bikkhasura has their spirit blades <br>  <br> **Effect** The bikkhasura directs one of its spirit blades to attack a target up to a distance of 50 feet away. Once a bikkhasura directs a spirit blade to attack a foe, the blade continues to make a single attack against that foe each round on the bikkhasura's turn until directed otherwise by the bikkhasura and as long as the foe remains within 50 feet of the bikkhasura. These weapons attack using the same statistics as the bikkhasura's spirit blade Strike and use the bikkhasura's multiple attack penalty. Any blades that are not within 50 feet of the bikkhasura at the end of its turn vanish."
  - name: "Glorious Visage"
    desc: "`pf2:1` The asura sanctifies themselves as either holy or unholy, gaining the trait corresponding to their choice and losing the opposing trait; their strikes, spells, and abilities also gain the trait corresponding to their choice. The asura also gains weakness 15 to the opposing sanctification and loses any weakness to its chosen sanctification. The choice is permanent until the asura uses this ability to change their sanctification."
  - name: "Spirit Blades"
    desc: "`pf2:1` **Frequency** once per hour <br>  <br> **Effect** The bikkhasura summons six blades made out of spiritual energy. The blades either appear in the bikkhasura's hands or foat next to the bikkhasura until the asura directs one or spends an Interact action to grab it. The spirit blades can be dispelled with a successful counteract check (counteract rank 10, counteract DC 42). A successful counteract dispels all blades, even if some have been directed away from the bikkhasura."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Asura who have been forcibly reincarnated across countless lifetimes, bikkhasuras have grown to nearly godlike levels of power.

```statblock
creature: "Bikkhasura"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
