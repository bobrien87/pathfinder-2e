---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Evangelist"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Greater Darkvision]]"
languages: "Common, Diabolic, Shadowtongue"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +15, Crafting +10, Intimidation +15, Religion +11, Torture Lore +12"
abilityMods: ["+4", "+3", "+2", "+0", "+1", "+1"]
abilities_top:
  - name: "Painsight"
    desc: "A velstrac automatically knows whether a creature it sees has any of the [[Doomed]], [[Dying]], and [[Wounded]] conditions as well as the value of those conditions."
  - name: "Grievous Wound"
    desc: "When the evangelist critically hits with a morningstar Strike, the target's wound is particularly gruesome and disorienting. The creature becomes [[Clumsy]] 1, and the DC to recover from its persistent bleed damage is 17 (DC 12 when receiving especially appropriate assistance). The clumsy condition doesn't end until the creature recovers from its persistent bleed."
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +14, **Will** +11"
health:
  - name: HP
    desc: "90; **Immunities** cold; **Weaknesses** holy 5, silver 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 10 (Deactivated by Holy or Silver)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Unnerving Gaze"
    desc: "30 feet. When a creature ends its turn in the aura, it sees the face of a departed loved one in place of the evangelist's face. The creature must succeed at a DC 21 [[Will]] save or become [[Frightened]] 2 ([[Frightened]] 3 on a critical failure)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Morningstar +17 (`pf2:1`) (magical, unholy, versatile p), **Damage** 2d6+7 bludgeoning plus 1d6 bleed plus [[Grievous Wound]]"
spellcasting: []
abilities_bot:
  - name: "Focus Gaze"
    desc: "`pf2:1` The evangelist stares at a creature they can see within 30 feet. The target must immediately attempt a DC 21 [[Will]] save against unnerving gaze. In addition, if the creature was already [[Frightened]], on a failed save, the evangelist is [[Concealed]] from the creature for as long as the creature remains frightened. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the evangelist's next turn."
  - name: "Unleash Weapon"
    desc: "`pf2:2` The evangelist releases their morningstar and commands the augur trapped within to attack. The weapon flies off and the evangelist makes up to two morningstar Strikes, each against a different target within 20 feet. These attacks count against the evangelist's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks. The morningstar then returns to the evangelist's hand."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Evangelists, the velstracs' unofficial ambassadors, roam the farthest reaches of the planes to spread the word of their kind's abhorrent belief in perfection through pain. They're therefore the most frequently encountered velstracs in the Universe, leading covens of hedonistic mortal flesh-sculptors or serving as wardens of horrific dungeons. In regions ruled by infernal powers, evangelists might serve as lieutenants or advisors, whispering secret paths to power in exchange for mortals' souls or choice mortal flesh. Evangelists are the same size as humans, although with their flesh transformed into something resembling a mockery of aristocratic raiments, and they often weigh 350 pounds or more.

The shadow-dwelling fiends known as velstracs all share a horrifying preoccupation with the search for ultimate sensation through self-mutilation. Velstracs transcend their stoic detachment only when inflicting pain and terror upon their victims, practicing new forms of torture, or turning their agonizing practices back on themselves. They consider themselves enlightened beings, transcending such limitations as morality or mortal taboos, but their victims know them as emotionless tormentors who inflict sadistic suffering. These fiends claim to seek perfection in thought, form, and action, although they don't recognize any refinement that doesn't require the painful excision of the flesh or spirit. Velstracs manifest from the souls of the most extreme masochistic or sadistic mortals who are judged and sent on to the Netherworld. They take on forms that suit their vile predilections, ranging from the low-ranking augurs to the maestros of suffering and mutilation, the eremites. The process of transformation warps the soul step by step, with other velstracs conveying their new members through untold chambers of pain among the dark reaches of the Netherworld.

```statblock
creature: "Evangelist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
